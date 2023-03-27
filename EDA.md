For this project, I have selected the dataset US births. This dataset can be found here: https://www.kaggle.com/datasets/des137/us-births-2018

I have performed EDA on this dataset by first training the model using the optimum regressor from the sklearn library, and then analysed using SHAP values.

The mse values for different regressors in comparison: 

LinearRegression: 0.9466729083191173

GradientBoostingRegressor: 0.8585813966180644

ElasticNet: 0.9890670373738261

SGDRegressor: 0.9494093321665038

CatBoostRegressor: 0.8711692582450455

XGBRegressor: 0.9105597975699139

LGBMRegressor: 0.8631553696562261

Comparing above, I decided to use Gradient Boosting Regressor as my main model on which SHAP values were applied. 

ANALYSIS: 

![image](https://user-images.githubusercontent.com/93089131/227852712-3353c97e-6356-4df3-9469-9e3019f94b8d.png)

The above is a SHAP tree explainer model. We can infer the most significant features which affect the target variable from this image. 

As we see, the most important features of our model are the delivery weight (DWgt_R), the number of prenatal visits (PREVIS), and the risk factors reported (NO_RISK).

Now, let's look at each of the feature independently to get a better understanding of the effect it has on our predicted birth weight.

![image](https://user-images.githubusercontent.com/93089131/227853115-4e63dc8d-5502-45d1-8eec-108ea8a7816f.png)

Interestingly, we can see that the maximal newborn baby weights correspond to mother delivery weights of about 280–300 pounds (127–136 kg), with a small subsequent decrease after these values:

![image](https://user-images.githubusercontent.com/93089131/227853154-c131f438-3c04-4154-b302-df91fd66f72b.png)

Remarkably, the baby’s weight peaks for about 15 prenatal care visits (PREVIS variable):

![image](https://user-images.githubusercontent.com/93089131/227853267-a3b5a841-d79d-419d-9103-5e7de6aa281e.png)

Not surprisingly, the absence of known risks (NO_RISKS variable) increases baby weight by about 0.21 kg on average

![image](https://user-images.githubusercontent.com/93089131/227853584-68f432f9-5c2b-49b2-aade-56c53e61728e.png)

Another important factor is baby gender (SEX variable), with male newborns having on average about 0.105 kg higher weights than female newborns:

![image](https://user-images.githubusercontent.com/93089131/227853620-bcb8210d-dcd3-4920-ad5d-d1549e6158a2.png)

Remarkably, average baby weights also peak for the mother’s pre-pregnancy body mass index (BMI variable) at around 20

![image](https://user-images.githubusercontent.com/93089131/227853665-b91f4165-ec50-40a3-b4bb-1e82371da840.png)

Remarkably, the daily number of cigarettes before the pregnancy (CIG_0 variable) also has an impact on newborn baby weights, with about a 0.08 kg difference between smoking and non-smoking mothers
