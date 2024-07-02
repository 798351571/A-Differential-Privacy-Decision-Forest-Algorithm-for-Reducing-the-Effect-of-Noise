# A-Differential-Privacy-Decision-Forest-Algorithm-for-Reducing-the-Effect-of-Noise
## experimental environment
Conda python3.6
### DPDF-REN:
import numpy as np<br>
import random<br>
import pandas as pd<br>
import queue<br>
import json<br>
from time import time<br>
import openpyxl<br>
import os
### TpDPRF:
import multiprocessing<br>
import random<br>
from collections import defaultdict<br>
import math<br>
import numpy as np<br>
import pandas as pd<br>
from numba import jit<br>
from sklearn.metrics import precision_score, recall_score<br>
from sklearn.model_selection import train_test_split<br>
import openpyxl<br>
import os<br>
import warnings<br>
from collections import Counter<br>
from time import time
### SNR:
from collections import Counter, defaultdict<br>
import random<br>
import numpy as np<br>
import math<br>
import pandas as pd<br>
import openpyxl<br>
import os

## Datasets

 Dataset  | Number of samples  |  Number of attributes  |  Number of classes
 ---- | ----- | ------  | ------
 Adult  | 48842 | 14 | 2
 Mushroom  | 8124 | 22 | 2
 Pima  | 768 | 9 | 2
 Car  | 1728 | 6 | 4
 ## Experiments
 Compare and contrast methods:TpDPRF[15],SNR[7]
  ## Reference
1. Bache, K., Lichman, M.: Uci machine learning repository (2013)
2. Blum, A., Dwork, C., McSherry, F., Nissim, K.: Practical privacy: the sulq framework. In: Proceedings of the Twenty-Fourth ACM SIGMOD-SIGACT-SIGART
Symposium on Principles of Database Systems. p. 128–138. PODS ’05, Association for Computing Machinery, New York, NY, USA (2005)
3. Dong, Y., Zhang, S., Xu, J., Wang, H., Liu, J.: Random forest algorithm based on
linear privacy budget allocation. J. Database Manage. 33(2), 1–19 (aug 2022)
4. Dwork, C.: Differential privacy. In: Proceedings of the 33rd International Conference on Automata, Languages and Programming - Volume Part II. p. 1–12.
ICALP’06, Springer-Verlag, Berlin, Heidelberg (2006)
5. Dwork, C., McSherry, F., Nissim, K., Smith, A.: Calibrating noise to sensitivity
in private data analysis. In: Proceedings of the Third Conference on Theory of
Cryptography. p. 265–284. TCC’06, Springer-Verlag, Berlin, Heidelberg (2006)
6. Dwork, C., Roth, A.: The Algorithmic Foundations of Differential Privacy (2014)
7. Fletcher, S., Islam, M.Z.: A differentially private random decision forest using
reliable signal-to-noise ratios. In: Pfahringer, B., Renz, J. (eds.) AI 2015: Advances
in Artificial Intelligence. pp. 192–203. Springer International Publishing, Cham
(2015)
8. Fletcher, S., Islam, M.Z.: Differentially private random decision forests using
smooth sensitivity. Expert Systems with Applications 78, 16–31 (2017)
9. Fletcher, S., Islam, M.Z.: Decision tree classification with differential privacy: A
survey. ACM Comput. Surv. 52(4) (aug 2019)
10. Friedman, A., Schuster, A.: Data mining with differential privacy. In: Proceedings
of the 16th ACM SIGKDD International Conference on Knowledge Discovery and
Data Mining. p. 493–502. KDD ’10, Association for Computing Machinery, New
York, NY, USA (2010)
11. Huang, Z., Lei, Y., Kabán, A.: Noise-efficient learning of differentially private partitioning machine ensembles. In: ECML/PKDD (2022)
12. Jagannathan, G., Pillaipakkamnatt, K., Wright, R.N.: A practical differentially
private random decision tree classifier. Trans. Data Privacy 5(1), 273–295 (apr
2012)
13. Li, X., Qin, B., Luo, Y., Zheng, D.: A differential privacy budget allocation algorithm based on out-of-bag estimation in random forest. Mathematics 10(22)
(2022)
14. Li, Y., Feng, Y., Qian, Q.: Fdpboost: Federated differential privacy gradient boosting decision trees. Journal of Information Security and Applications 74, 103468
(2023)
15. Liu, J., Li, X., Wei, Q., Liu, S., Liu, Z., Wang, J.: A two-phase random forest with
differential privacy. Applied Intelligence 53(10), 13037–13051 (oct 2022)
16. Liu, X., Li, Q., Li, T., Chen, D.: Differentially private classification with decision
tree ensemble. Applied Soft Computing 62, 807–816 (2018)
17. Liu, Y., Fan, Z., Song, X., Shibasaki, R.: Fedvoting: A cross-silo boosting tree
construction method for privacy-preserving long-term human mobility prediction.
Sensors 21(24) (2021)
18. Manzali, Y., Akhiat, Y., Chahhou, M., Elmohajir, M., Zinedine, A.: Reducing the
number of trees in a forest using noisy features. Evolving Systems 14, 157–174
(2022)
19. McSherry, F.: Privacy integrated queries: an extensible platform for privacypreserving data analysis. Commun. ACM 53(9), 89–97 (sep 2010)
20. McSherry, F., Talwar, K.: Mechanism design via differential privacy. In: 48th Annual IEEE Symposium on Foundations of Computer Science (FOCS’07). pp. 94–
103 (2007)
21. Mohammed, N., Chen, R., Fung, B.C., Yu, P.S.: Differentially private data release
for data mining. In: Proceedings of the 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. p. 493–501. KDD ’11, Association
for Computing Machinery, New York, NY, USA (2011)
22. Niu, X., Ma, W.: An ensemble learning model based on differentially private decision tree. Complex & Intelligent Systems pp. 1–14 (2023)
23. Quinlan, J.R.: C4.5: Programs for Machine Learning. Morgan Kaufmann Publishers Inc., San Francisco, CA, USA (1993)
24. Tayefi, M., Tajfard, M., Saffar, S., Hanachi, P., Amirabadizadeh, A.R., Esmaeily,
H., Taghipour, A., Ferns, G.A., Moohebati, M., Ghayour-Mobarhan, M.: hs-crp
is strongly associated with coronary heart disease (chd): A data mining approach
using decision tree algorithm. Computer Methods and Programs in Biomedicine
141, 105–109 (2017)
25. Wang, C., Chen, S., cheng Li, X.: Adaptive differential privacy budget allocation
algorithm based on random forest. In: International Conference on Bio-Inspired
Computing: Theories and Applications (2021)
26. Wang, R., Fung, B.C., Zhu, Y.: Heterogeneous data release for cluster analysis
with differential privacy. Knowledge-Based Systems 201-202, 106047 (2020)
27. Wu, X., Qi, L., Gao, J., Ji, G., Xu, X.: An ensemble of random decision trees with
local differential privacy in edge computing. Neurocomputing 485, 181–195 (2022)
 
