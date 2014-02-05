import classifier.lstm.util as util
import numpy as np
from scipy import stats as stats
from systemkeys import SystemKeys

'''
LSTMCLassify class provides different methods for live/online classification with the LSTM Module. 
It also calls the Systemkeys class to bind keys to classes and execute the bindings
'''
class LSTMClassify():

    def __init__(self, config, net):
        self.config = config
        self.net = net
        self.avg = util.getAverage(self.net.datacut, self.net.datafold)

        self.datalist = []
        self.datanum = 0
        self.has32 = False
        self.previouspredict = 6
        self.predcounter = 0
        self.predHistSize = 8
        self.predHistHalfUpper = 5
        self.predHistory = util.createArraySix(self.predHistSize,)

        # Classify3 method
        self.predhistoryforclassify3 = []

        self.outkeys = SystemKeys()

    '''
    Interface method for classifcation. WIll be called by LSTM interface and calls different implementations. 
    Preprocess data. 
    '''
    def classify(self, data):
        preprocessedData = data / np.amax(data)
        preprocessedData = util.preprocessFrame(preprocessedData, self.net.datacut, self.net.datafold)
        diffAvgData = preprocessedData - self.avg
        self.__classify2(diffAvgData)

    '''
    Gesten werden starr nach 32 frames erkannt
    '''
    def __classify1(self, data):
        self.datalist.append(data)
        self.datanum += 1
        if(self.datanum % 32 == 0):
            self.net.reset()
            out = self.net._activateSequence(self.datalist)
            print(str(out))
            self.datalist = []
            self.datanum = 0
            return out
        return -1

    '''
    Gesten werden auf folgende Art erkannt:
    - wenn 32 Datensaetze vorhanden sind wird das Netz aktiviert und der Output in eine Liste gespeichert
    - Diese Liste wird staendig erweitert und hat ein feste Laenge (siehe self.predHistory in init)
    - Es wird der Modus der Liste gebildet
    - Ist der Modus ueber einem  bestimmten Treshold (self.predHistHalfUpper) wird der Wert in self.previouspredict gespeichert
    - Ist previouspredict 4 mal gleich wird die Gestenklasse ausgegeben, ist die Klasse groesser als 4 mal gleich erfolgt keine neue Ausgabe
    - 
    '''
    def __classify2(self, data):
        self.datanum += 1
        self.datalist.append(data)
        if(self.datanum % 32 == 0):
            self.has32 = True
        if(self.has32):
            self.net.reset()
            Y_pred = self.net._activateSequence(self.datalist)
            del self.datalist[0]
            self.predHistory[0] = Y_pred
            self.predHistory = np.roll(self.predHistory, -1)
            expected = stats.mode(self.predHistory, 0)
            if(expected[1][0] >= self.predHistHalfUpper):
                if(int(expected[0][0]) != self.previouspredict):
                    oldPrevious, oldPredCounter = self.previouspredict, self.previouspredict
                    self.previouspredict = int(expected[0][0])
                    self.predcounter = 1
                    return oldPrevious, oldPredCounter
                else:
                    self.predcounter += 1
                    if(self.predcounter == 4):
                        print(str(self.previouspredict))
                        self.outkeys.outForClass(self.previouspredict)
                    return self.previouspredict, self.predcounter
        return -1, -1


    '''
    Gesten werden innerhalb von der Geste 6 gesucht
    TODO not finished yet
    '''
    def __classify3(self, data):
        pred, predcounter = self.__classifiy2(data)
        if(pred != -1 and predcounter >= 4):
            try:
                prevpred, prevpredcounter = self.predhistoryforclassify3.pop()
                if(prevpred != pred):
                    self.predhistoryforclassify3.append([prevpred, prevpredcounter])
            except IndexError:
                pass
            self.predhistoryforclassify3.append([pred, predcounter])
            if(pred == 6 and len(self.predhistoryforclassify3) <= 1):
                pass
            else:
                classes = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
                for pred, count in self.predhistoryforclassify3:
                    classes[pred] += count
                classes.pop(6)
                classifiedclass = stats.mode(np.asarray(classes.values()), 0)
                print(str(classifiedclass))


    '''
    Gesten werden anhand eines erkannten Starttresholds erkannt
    '''
    def __classify4(self, data):
        # sequence maximum erkennen
        pass
