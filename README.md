# Awesome Face Recognition

[2019.12.04 - Debugging Log] 

* Decoupled Network
  * I am trying to implementation DecoupledNetwork on https://github.com/ChoSungMan/DCNets-pytorch
  

---



## Implementation 

### Datasets

**- Training**
- [x] Faces-emore

  

**- Evaluation**
- [x] LFW
- [x] Agedb-30
- [x] CFP-FP



### Implemented Networks

- [ ] [CVPR 2018] Decoupled Networks
- [x] [CVPR 2019] Arcface 
- [x] [CVPR 2019] Regularface



### How to train ?

1. Set-up virtual environment.  

   ```
   conda create -n [your environment] python=3.6
   
   source activate [your environment]
   
   conda install pytorch cuda90 torchvision -c pytorch
   
   pip install -r requirements.txt
   ```

2. Download train, test datasets  
   ( https://github.com/TreB1eN/InsightFace_Pytorch —> 3.1 Data Preparation )  

3. Training 
   `python train.py --train_root [your data root] --epochs [epochs] --batch_size [batch_size] --save_root [root for saving weights, log file]`



### Modules (TO DO)

- [x] Decoupled Operators
- [ ] Feature Visualization Module
- [ ] Simple Test GUI (face registration, face detection, face recognition)





## References

1. <https://github.com/TreB1eN/InsightFace_Pytorch>
2. https://github.com/ronghuaiyang/arcface-pytorch
3. https://github.com/wy1iu/DCNets

