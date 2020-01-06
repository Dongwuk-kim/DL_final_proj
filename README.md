# DL_final_proj

hi

Deep Learning final project istical arbitrage

- Common work : Developing clustering algorithms, Presentation
- Kim Seung Kyu : Obtaining data, Coding k-means algorithm, Theoretical support 
- Kim Dong Wuk : Preprocessing finance data, Construct backtesting environment
- Kim Chang Kyeom : Preprocessing data, simple deep-learning methods


1. ## Purpose

   A statistical arbitrage refers to a highly technical short-term mean-reversion strategy involving a large number of securities (Lo, 2010). Roughly speaking, the main idea of the mean-reversion is to first find a common trend within a group, then ‘sell’ the stocks whose returns are greater than the mean, and ‘buy’ the underperforming ones. This strategy can gain profit if one believes that all returns of specific securities will eventually converge to the main trend of that group. The existing strategies use information of sectors or industry provided by data-vendors when forming groups. Also, recent research investigated on a possibility of performance gain by using K-means clustering to classify the individual corporations into groups (Kakushadze, 2016). In this project, we will adapt parametric deep learning models for grouping method on mean-reversion strategy.

2. ## Significance of this research

   In this field of research, there are two main limitations:
   Little is known about classification methods of industries that boosts the performance, contrary to strategies which construct portfolio models that aim to maximize profits.
   Many research is conducted with the assumption that clustering results are available a priori, and such result is mostly provided via the vendors who supply the data. (There are some attempts that uses nonparametric clustering methods, such as K-means clustering. (Kakushadze and Yu, 2016))

   These, unfortunately, may hinder the performance of the mean-reversion model. Take Apple, for example, which belongs to a “computer hardware” sector and “consumer electronics” industry according to ‘morningstar’, one of the vendors. However, considering that Apple focuses on both hardware and software, this classification may lead to suboptimal results.
   Therefore, we intend to provide an improved variant of mean-reversion strategy by providing clustering algorithms based on parametric models (and we will use deep learning methods). We anticipate this approach to mitigate the two limitations above.

3. ## Data preprocessing

   Acquiring Data (daily price of US equities, Fundamental data, BIC informations,...)
   Mapping Sector/industry information with securities
   Backtesting basic mean-reversion algorithm
   Implement K-means clustering with mean-reversion algorithm
   Developing/training deep learning model
   Design loss function(Aim to profit maximization)
   Training deep learning model (Auto-encoder, RNN,..etc)
   Comparing and Plotting the performance in testset(Profit and loss, Sharp ratio,..)

4. ## Team member information

   Common work : Developing clustering algorithms, Presentation
   Kim Seung Kyu : Obtaining data, Coding k-means algorithm, Theoretical support 
   Kim Dong Wuk : Preprocessing finance data, Construct backtesting environment
   Kim Chang Kyeom : Preprocessing data, simple deep-learning methods



5. ## Specific plan

   1. **Understanding and constructing the building block( 11/10~11/19)**

   - Acquiring/preprocessing Finance Data
   - Construct backtesting environment
   - Paper study(optimization with factor model, clustering model) 
   - Implement algorithms 

   2. **Implement algorithms(11/19~11/24) **

   - K-means algorithm
   - Mean reversion with optimization
   - Simple clustering model with loss function
   - 

   3. **Developing clustering algorithms(11/24~12/04) **

   - modify deep-learning algorithm


      3. **Result(12/05~12/08) **

   - Comparison and visualization of the performance

      4. **Presentation(12/09~12/11)**

   - Present the results
   - Comparison and visualization of the performance


      1. **Understanding and constructing the building block**- Present the results
   2. Reference
      Kakushadze, Z. (2014). Mean-reversion and optimization. Journal of Asset Management, 16(1), 14-40.
      Kakushadze, Z., & Yu, W. (2016). Statistical industry classification. Journal of Risk & Control, 3(1), 17-65.
      Lo, A. W. (2010). Hedge Funds: An Analytic Perspective-Updated Edition (Vol. 3). Princeton University Press.
      Min, E., Guo, X., Liu, Q., Zhang, G., Cui, J., & Long, J. (2018). A survey of clustering with deep learning: From the perspective of network architecture. IEEE Access, 6, 39501-39514.
