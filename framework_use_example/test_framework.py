from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from data_preprocessing_framework.data_pipeline import DataPipeline


def logistic_regression(train_inputs, train_outputs, test_inputs, test_outputs):
    regressor = LogisticRegression(max_iter=1000, multi_class='ovr')
    regressor.fit(train_inputs, train_outputs.ravel())
    tool_output = regressor.predict(test_inputs)
    print("Error sklearn:")
    error(test_outputs, tool_output)


def error(test_outputs, computed_test_outputs):
    toolError = 1 - accuracy_score(test_outputs, computed_test_outputs)
    print('Tool error : ' + str(toolError))

def main():
    data_pipeline = DataPipeline("../data_pipeline_config.ini")
    train_inputs, train_outputs, test_inputs, test_outputs = data_pipeline.preprocess_data()
    logistic_regression(train_inputs, train_outputs, test_inputs, test_outputs)

main()