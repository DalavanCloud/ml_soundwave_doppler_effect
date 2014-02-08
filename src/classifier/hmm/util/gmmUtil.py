import numpy as np
import sys
import classifier.hmm.config.config as c

from classifier.hmm.gestureGMM import GestureGMM

class GMM_Util():
    '''
    class for training gmms
    
    n_components  = Number of mixture components
    
    n_iter        = Number of EM iterations to perform.
    
    n_init        = Number of initializations to perform. the best results is kept

    '''
    
    
    def __init__(self, n_components = c.n_components_gmm, covariance_type=c.covariance_type_gmm, n_iter = c.n_iter_gmm, n_init = c.n_init_gmm):
        self.n_components = n_components
        self.covariance_type = covariance_type
        self.n_iter = n_iter
        self.n_init = n_init
        self._gmms = []


    def trainGmms(self, data):
        '''
        returns trained gmms
        
        data    = np.arry-like: 
        data     :  [ 
        gesture  :    [
        frames   :      [ 0, 1, 2, 3, ... , n_bin], #0
                        [ 0, 1, 2, 3, ... , n_bin], #1
                        ...
                        [ 0, 1, 2, 3, ... , n_bin] #i_frame
                      ],
                      [
                        [ 0, 1, 2, 3, ... , n_bin], #0
                        [ 0, 1, 2, 3, ... , n_bin], #1
                        ...
                        [ 0, 1, 2, 3, ... , n_bin] #i_frame
                      ]
                    ]
        '''
        n_frames = len(data[0])
        cData = self._convertData(data)
        for i in range(n_frames):
            self._gmms.append(self._train(cData[i]))
        return self._gmms

    def _averageScore(self, gmm, test):
        return np.average(gmm.score(test))

    def _train(self, data):
        logprob = -sys.maxint - 1
        gmm = None
        i = 0
        while logprob < c.logprobBound_gmm:
            g = GestureGMM(self.n_components, covariance_type=self.covariance_type, init_params='', n_iter=self.n_iter, n_init=self.n_init)
            g.fit(data)
            l = self._averageScore(g, data)
            if 0 > l > logprob:
                logprob = l
                gmm = g
            i += 1
            if i >= c.n_tries_gmm:
                break
        return gmm
        

    def testGmms(self, data):
        '''
        tests given gmms
        '''
        
        n_frames = len(data[0])
        cData = self._convertData(data)
        means = []
        for i in range(n_frames):
            means.append(np.mean(self._gmms[i].score(cData[i])))
        return means

    # DATA
    def _convertData(self, data):
        '''
        returns converted data 
        
        returns    = np.arry-like: 
        data     :  [ 
        class    :    [
        frames   :      [ 0, 1, 2, 3, ... , n_bin], #0
                        [ 0, 1, 2, 3, ... , n_bin], #0
                        ...
                        [ 0, 1, 2, 3, ... , n_bin]  #0
                      ],
                      [
                        [ 0, 1, 2, 3, ... , n_bin], #1
                        [ 0, 1, 2, 3, ... , n_bin], #1
                        ...
                        [ 0, 1, 2, 3, ... , n_bin]  #1
                      ]
                    ]
        
        
        '''
        n_frames = len(data[0])
        cData = [[] for i in range(n_frames)]
        for i in range(n_frames):
            for gesture in data:
                cData[i].append(list(gesture[i]))
        return np.array(cData)


    def sample(self, data):
        self.trainGmms(data)
        return self._gmms