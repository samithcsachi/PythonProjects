import random

questions = {
    # General Machine Learning & Foundations
    "What type of learning uses labeled data?": "supervised",
    "What type of learning finds hidden patterns in unlabeled data?": "unsupervised",
    "What type of learning learns via rewards and penalties?": "reinforcement",
    "What is the term for a machine learning model performing well on training data but poorly on test data?": "overfitting",
    "What is the term for a model that is too simple to capture the underlying pattern?": "underfitting",
    "Which plot helps visualize model performance on binary classification?": "roc curve",
    "What matrix shows True Positives, False Positives, True Negatives, and False Negatives?": "confusion matrix",
    "What metric measures the proportion of correctly predicted instances over total instances?": "accuracy",
    "What metric measures True Positives divided by True Positives plus False Positives?": "precision",
    "What metric measures True Positives divided by True Positives plus False Negatives?": "recall",
    "What metric is the harmonic mean of precision and recall?": "f1-score",
    "What is the process of normalizing feature values into a common range?": "feature scaling",
    "Which technique drops features or penalizes complexity to prevent overfitting?": "regularization",
    "What type of regularization adds an L1 penalty to loss function?": "lasso",
    "What type of regularization adds an L2 penalty to loss function?": "ridge",
    "What algorithm finds optimal model parameters by iteratively moving in the direction of steepest descent?": "gradient descent",
    "What hyperparameter controls the step size at each iteration in gradient descent?": "learning rate",
    "What technique splits a dataset into K subsets for cross-validation?": "k-fold",
    "What is the process of selecting the best parameters for an ML algorithm?": "hyperparameter tuning",
    "What technique reduces dataset dimensionality while preserving maximum variance?": "pca",

    # Classical ML Algorithms
    "Which linear algorithm is used for predicting continuous numeric values?": "linear regression",
    "Which linear model uses the sigmoid function to output probabilities for classification?": "logistic regression",
    "Which tree-based algorithm splits data based on conditions like Gini impurity or Entropy?": "decision tree",
    "Which ensemble algorithm builds multiple decision trees using bootstrap aggregating (bagging)?": "random forest",
    "What algorithm finds a hyperplane that maximizes the margin between classes?": "svm",
    "What non-parametric algorithm classifies samples based on the majority vote of nearby points?": "knn",
    "What probabilistic classifier is based on applying Bayes' theorem with strong independence assumptions?": "naive bayes",
    "What unsupervised algorithm partitions data into K distinct clusters based on distance?": "k-means",
    "What algorithm uses density to discover clusters of arbitrary shapes and identify noise?": "dbscan",
    "Which ensemble framework sequentially trains weak learners to correct errors of previous trees?": "gradient boosting",
    "What popular gradient boosting library is known for speed and performance in ML competitions?": "xgboost",
    "What LightGBM competitor library is optimized for handling categorical features automatically?": "catboost",
    "What metric measures the impurity of a dataset in Decision Trees alongside Gini?": "entropy",
    "What is the process of removing branches from a decision tree to reduce overfitting?": "pruning",
    "What distance metric is most commonly used in K-Means clustering?": "euclidean",

    # Data Preprocessing & Feature Engineering
    "What encoding technique converts categorical variables into binary 0/1 columns?": "one-hot",
    "What encoding technique converts categories into sequential numerical IDs?": "label encoding",
    "What scaling technique reshapes values to have mean 0 and standard deviation 1?": "standardization",
    "What scaling technique rescales features to a fixed range, usually 0 to 1?": "min-max scaling",
    "What term describes missing data or incomplete records in a dataset?": "null values",
    "What process replaces missing dataset values with estimated ones like mean or median?": "imputation",
    "What data imbalance issue occurs when one class far outnumbers another?": "class imbalance",
    "What popular oversampling method generates synthetic samples for the minority class?": "smote",

    # Neural Network Fundamentals
    "What is the basic computational unit or building block of a neural network?": "perceptron",
    "What function introduces non-linearity into a neural network layer?": "activation function",
    "Which activation function outputs values between 0 and 1?": "sigmoid",
    "Which activation function outputs values between -1 and 1?": "tanh",
    "Which activation function replaces negative inputs with zero and keeps positive inputs unchanged?": "relu",
    "Which variant of ReLU allows a small positive gradient for negative inputs?": "leaky relu",
    "Which activation function converts raw logits into a probability distribution for multi-class classification?": "softmax",
    "What algorithm computes gradients of the loss function using the chain rule?": "backpropagation",
    "What loss function is standard for binary classification problems in neural networks?": "binary cross-entropy",
    "What loss function is standard for multi-class classification problems?": "categorical cross-entropy",
    "What loss function calculates the average squared difference between predictions and actual values?": "mse",
    "What loss function calculates the average absolute difference between predictions and actual values?": "mae",
    "What term refers to one complete pass through the entire training dataset?": "epoch",
    "What is the number of training samples processed in one forward/backward pass?": "batch size",

    # Deep Learning Concepts & Training
    "What problem occurs when gradients become extremely small during backpropagation in deep networks?": "vanishing gradient",
    "What problem occurs when gradients become excessively large, causing unstable updates?": "exploding gradient",
    "What regularization technique randomly deactivates neurons during training to prevent co-adaptation?": "dropout",
    "What technique normalizes activation outputs of intermediate layers within mini-batches?": "batch normalization",
    "What gradient descent variant updates parameters using a small random subset of data per step?": "stochastic gradient descent",
    "Which popular optimizer combines momentum and RMSprop principles?": "adam",
    "What technique stops neural network training when validation loss stops improving?": "early stopping",
    "What technique initializes weights from a pre-trained model on a large dataset?": "transfer learning",
    "What strategy adjusts the learning rate during training, such as lowering it over time?": "learning rate decay",

    # Convolutional Neural Networks (CNNs)
    "What type of neural network is specialized for processing grid-like data like images?": "cnn",
    "What matrix slides over an image to extract visual features in a CNN?": "kernel",
    "What operation applies a kernel over an input tensor to extract local features?": "convolution",
    "What CNN layer reduces spatial dimensions (width and height) of feature maps?": "pooling",
    "Which pooling operation selects the maximum value in a localized region?": "max pooling",
    "What term describes adding extra zero pixels around an input image border during convolution?": "padding",
    "What term describes the step size by which a convolution kernel slides across an image?": "stride",
    "What iconic CNN architecture won the ImageNet challenge in 2012, sparking the DL revolution?": "alexnet",
    "What CNN architecture family introduced residual skip connections to train ultra-deep networks?": "resnet",
    "Which light-weight CNN architecture is designed specifically for mobile and edge devices?": "mobilenet",

    # Recurrent Neural Networks & NLP
    "What type of neural network handles sequential data like text or time series using internal loops?": "rnn",
    "What specialized RNN architecture uses gates to retain long-term dependencies in sequences?": "lstm",
    "Which simplified gate-based RNN architecture combines the cell state and hidden state?": "gru",
    "What NLP technique converts words into dense numerical vector representations?": "word embedding",
    "What popular 2013 algorithm family produces word vectors like Continuous Bag of Words (CBOW)?": "word2vec",
    "What mechanism allows models to focus selectively on specific parts of an input sequence?": "attention",
    "What architecture, introduced in 2017, relies entirely on attention mechanisms without recurrence?": "transformer",
    "What bidirectional transformer model was pre-trained by Google on masked language modeling?": "bert",
    "What auto-regressive transformer model family was created by OpenAI for generative text?": "gpt",
    "What natural language processing task assigns labels like Positive or Negative to text?": "sentiment analysis",

    # Generative AI & Advanced DL
    "What framework uses a Generator and a Discriminator competing in a min-max game?": "gan",
    "What network component in a GAN attempts to synthesize realistic synthetic data?": "generator",
    "What network component in a GAN attempts to distinguish real data from generated data?": "discriminator",
    "What generative models learn latent representations by encoding inputs and decoding reconstructions?": "autoencoder",
    "What type of generative models add noise step-by-step and then learn to reverse the process?": "diffusion models",
    "What low-rank adaptation technique efficiently fine-tunes large language models with few parameters?": "lora",
    "What alignment technique uses human preferences to fine-tune language models?": "rlhf",

    # Tools, Frameworks & Hardware
    "What open-source deep learning framework was developed by Google?": "tensorflow",
    "What open-source deep learning framework is primary maintained by Meta and AI researchers?": "pytorch",
    "What high-level Python library runs on top of TensorFlow to simplify building neural networks?": "keras",
    "What classical ML library in Python contains models like Decision Trees, SVMs, and PCA?": "scikit-learn",
    "What specialized hardware chip, developed by NVIDIA, accelerates parallel matrix computation?": "gpu",
    "What custom ASIC hardware chip did Google create specifically for tensor operations?": "tpu",
    "What NVIDIA parallel computing platform allows software developers to run code directly on GPUs?": "cuda"
}



def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    for idx, question in enumerate(selected_questions):
        print(f"Question {idx +1} : {question}")
        user_answer = input("Your answer: ").strip().lower() 
        correct_answer = questions[question].lower()
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {questions[question]}\n")
    print(f"Game Over! Your score: {score}/{total_questions}")



def main():
    python_trivia_game()


if __name__ == "__main__":
    main()
