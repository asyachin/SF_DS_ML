# ALS-Based Recommender System

Our recommender system is built upon an **Implicit Alternating Least Squares (ALS)** base model, which utilizes a matrix factorization method derived from **Singular Value Decomposition (SVD)**.

## Input Data Format for Training

The input data consists of an online store's user session dataset, incorporating factors such as session time, user ID, product ID, session type (browsing, adding to cart, and purchasing), and purchase ID. No additional data was utilized beyond this dataset.

## Transformations of the Original Dataset

For training and validating the model, we focused on sessions from users who made purchases. All other users were not included in the model building process and were instead provided with a list of the most popular products.

## Dataset Filtering and Splitting

The filtered dataset was divided into training and validation sets using the `sklearn` library.

## System Architecture

The system employs a collaborative filtering approach using matrix factorization with the **Implicit ALS** method from the `implicit` library, a popular choice in building recommender systems.

## Technical Metrics

We used **Precision@3** as the technical metric, with an average value of **0.006475**. Model accuracy could potentially be improved with additional product properties and user ratings.

## Model Improvement Through Hyperparameter Tuning

The model's performance was enhanced by tuning hyperparameters. The best accuracy was achieved with the parameters: `best_params {'factors': 500, 'iterations': 3, 'regularization': 0.01}`.

## Efficiency for Web Service Implementation

To reduce response time in the web service recommendations, a dataframe was created containing users and the products recommended to them. Other users are recommended the most popular products.

## Web Service Deployment

The web service is also available as a Docker image:

```bash
docker pull u745/recsys_app:latest

To launch the container, use port 3000:
docker run -p 3000:3000 u745/recsys_app
