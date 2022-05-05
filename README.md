# RNN-Sales-Timeseries
This is a 2-stage process that uses Tensorflow and in particular the bundled Keras API to build and serve a Recurrent Neural Network (RNN) DL model to forecast about a sample time series on sales revenues.
<p>
First, run the Python script, rnn_sales_timeseries.py, provided by Dr Jason Browniee in https://machinelearningmastery.com/tensorflow-tutorial-deep-learning-with-tf-keras/ to build and evaluate an RNN DL model based on a sample of monthly car sales data points.
<p>
To avoid missing components or other issues in installing Tensorflow on a host system, it is suggested that the model builder script be run on a tensorflow/tensorflow container to save the model in a host-mounted volume.
<p>
<pre> 
docker run -it --name tfcontainer -v /root/RNN-Sales-Timeseries:/tensorflow tensorflow/tensorflow
cd /tensorflow
python3 rnn_sales_timeseries.py
</pre>
The model is consequently saved in /root/RNN-Sales-Timeseries/rnn_sales_timeseries_model on the host itself.
<p>
After that, deploy a tensorflow container to load and serve the model by predicting the sales revenues of a particular month based on the past 5 months, e.g.
<p>
<pre>
docker build -t yourname/rnn_sales_forecast:v1 -f Dockerfile .
docker push yourname/rnn_sales_forecast:v1
docker run -d --name prediction -p 5005:5005 yourname/rnn_sales_forecast:v1
</pre>
