# Laptop price analysis and price prediction
This project builds a machine learning model to predict and analyse laptop price. It involves data preprocessing, save piple line data, and save clean data for model training, evaluation, create a pipeline and Streamlit deployment.

---
## Project Structure

```
├── Data/                  
├── notebook/  
|    ├── catboost_info
|    ├── Visual.ipynb          
│    └── model_train.ipynb       
├── Model Deploy/
│   ├── app.py              
│   └── Xgb_model.pkl           
├── requirements.txt          
├── README.md   
├── Laptop price analysis.pbix        
├── .gitignore 
└── Report file
```

## Objective

To predict and analyse laptop price.
And create beautifull interface of Power BI report
---

## Features Used

- Company 
- Product	 
- TypeName	 
- Inches	 
- Ram	 
- OS	 
- Weight	 
- Price_euros	 
- Screen	 
- ScreenW	 
- ScreenH	 
- Touchscreen	 
- IPSpanel	 
- RetinaDisplay	
- CPU_company	  
- CPU_freq	 
- CPU_model	
- PrimaryStorage    
- SecondaryStorage    
- PrimaryStorageType    
- SecondaryStorageType    
- GPU_company   
- GPU_model    
---

##  Technologies Used

- Python (Pandas, NumPy, seaborn, matplotlib, Scikit-learn, Imbalanced-learn)
- Streamlit (for deployment)
- Joblib (for model saving/loading)
- Power BI (for creating beautifull interface to data analysis)

---

## Model & Evaluation

- **Model Used:** e.g., RandomForestRegressor / XGBoostRegressor
- **Evaluation Metrics:**
  - R2 score 
  - Adjusted r2, Mean absolute error, mean squared error, Cross val score
  - R2 gap

- **Issue Solved:** Fix Under fitting and analyse laptop price.

---

## How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/Priyanshu-techp/Laptop-price-analysis-and-price-prediction.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run "Model_deploy/app.py"
   ```
---

## Deploy link
[Streamlit app link](https://laptop-price-prediction-mod.streamlit.app/)

## Results

- **Best r2-score:** ~0.83  
- **Overall Accuracy:** ~0.83
- **R2 gap:** ~0.049  
- **Fix under fitting**

---

## Author

**Priyanshu Pandey**  
Diploma in Automation & Robotics  
Aspiring Data Scientist  
[LinkedIn Profile](https://www.linkedin.com/in/priyanshu-pandey67)
