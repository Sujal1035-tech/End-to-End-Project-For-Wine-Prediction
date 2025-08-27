# 🍷 End-to-End Wine Quality Prediction

A comprehensive machine learning pipeline that predicts wine quality based on physicochemical properties. This project implements a complete end-to-end ML workflow including data processing, model training, evaluation, and deployment through a web application.

---

## ✨ Features

• **Complete ML Pipeline** - From data ingestion to model deployment  
• **Wine Quality Classification** - Predict wine quality ratings  
• **Multiple Algorithm Comparison** - Compare various machine learning models  
• **Data Processing Pipeline** - Robust data validation and transformation  
• **Web Interface** - User-friendly prediction interface  
• **Configuration Management** - YAML-based flexible configuration system  
• **Modular Architecture** - Easily extensible and maintainable codebase  

---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### 1. Clone the repository
```bash
git clone https://github.com/Sujal1035-tech/End-to-End-Project-For-Wine-Prediction.git
cd End-to-End-Project-For-Wine-Prediction
```

### 2. Create virtual environment
```bash
conda create -n mlproj python=3.8 -y
conda activate mlproj
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

---

## 💻 Usage

### 🎯 Train the Model
```bash
python main.py
```

### 🌐 Access Web Interface
```bash
python app.py
```
**➡️ Open `http://localhost:8080` in your browser**

### 📊 Make Predictions
Enter wine characteristics such as:
- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- pH Level
- Alcohol Content

---

## 📁 Project Structure

```
End-to-End-Project-For-Wine-Prediction/
│
├── 📂 config/                 # Configuration files
│   ├── ⚙️ config.yaml
│   ├── 🔧 params.yaml
│   └── 📋 schema.yaml
│
├── 📦 artifacts/              # Generated model artifacts
│   ├── 📥 data_ingestion/
│   ├── ✅ data_validation/
│   ├── 🔄 data_transformation/
│   ├── 🤖 model_trainer/
│   └── 📊 model_evaluation/
│
├── 🔍 src/mlProject/         # Source code
│   ├── 🧩 components/        # Pipeline components
│   ├── 🔄 pipeline/          # Training and prediction pipelines
│   ├── 🛠️ utils/             # Utility functions
│   └── ⚙️ config/            # Configuration management
│
├── 🎨 templates/             # HTML templates
├── 📄 static/                # CSS and JavaScript files
├── 📊 research/              # Jupyter notebooks for experimentation
├── 🖥️ app.py                 # Flask web application
├── 🚂 main.py                # Training pipeline entry point
├── 🐳 Dockerfile             # Docker configuration
└── 📜 requirements.txt       # Project dependencies
```

---

## 🔄 Pipeline Components

| **Stage** | **Description** |
|-----------|-----------------|
| **1️⃣ Data Ingestion** | Downloads and loads wine quality dataset |
| **2️⃣ Data Validation** | Schema validation and data quality checks |
| **3️⃣ Data Transformation** | Feature scaling and preprocessing |
| **4️⃣ Model Training** | Multiple algorithms with hyperparameter tuning |
| **5️⃣ Model Evaluation** | Performance metrics and model comparison |
| **6️⃣ Model Deployment** | Flask web application with prediction API |

---

## ⚙️ Configuration

| **File** | **Purpose** |
|----------|-------------|
| 📝 `config.yaml` | Data sources and pipeline settings |
| 🎛️ `params.yaml` | Model hyperparameters |
| ✅ `schema.yaml` | Data validation rules |

---

## 🌐 Web Application

The Flask app provides:

• **📝 Interactive Form** - Input wine characteristics easily  
• **⚡ Real-Time Predictions** - Instant quality predictions  
• **📊 Quality Scoring** - Wine quality ratings from 3-9  
• **🎨 Responsive Design** - Works on desktop and mobile devices  
• **📈 Confidence Scores** - Model prediction confidence levels  

---

## 🤖 Model Performance

The project implements and compares multiple algorithms:

| **Algorithm** | **Type** |
|---------------|----------|
| 📈 **Linear Regression** | Linear Model |
| 🌳 **Decision Tree** | Tree-based |
| 🌲 **Random Forest** | Ensemble Method |
| 🚀 **Gradient Boosting** | Boosting Algorithm |
| 🎯 **Support Vector Machine** | Kernel-based |
| 🔍 **K-Nearest Neighbors** | Instance-based |

### 📈 Model Results

**🏆 Best Performing Model: Random Forest Regressor**

| **Metric** | **Score** |
|------------|-----------|
| 🎯 **R² Score** | 0.85+ |
| 📊 **MAE** | < 0.5 |
| 🔍 **RMSE** | < 0.7 |

📊 **Detailed performance metrics are generated during training and stored in the artifacts directory.**

---

## 🍷 Dataset Information

The project uses the **Wine Quality Dataset** containing:

• **📊 Features**: 11 physicochemical properties  
• **🎯 Target**: Wine quality rating (3-9)  
• **📈 Samples**: 1599+ wine samples  
• **🔍 Type**: Regression/Classification problem  

### Wine Features:
- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

## 🤝 Contributing

We welcome contributions! Here's how:

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch
3. **✨ Make** your changes
4. **📤 Submit** a pull request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📞 Contact

**👨‍💻 Sujal** - [GitHub Profile](https://github.com/Sujal1035-tech)

Project Link: [https://github.com/Sujal1035-tech/End-to-End-Project-For-Wine-Prediction](https://github.com/Sujal1035-tech/End-to-End-Project-For-Wine-Prediction)

---

## 🎯 Future Enhancements

• **📱 Mobile App** - React Native mobile application  
• **☁️ Cloud Deployment** - AWS/Azure deployment  
• **🤖 AutoML** - Automated model selection  
• **📊 Advanced Visualization** - Interactive charts and graphs  
• **🔄 Real-time Updates** - Live model retraining  

---

⭐ **If you find this project helpful, please give it a star!** ⭐
