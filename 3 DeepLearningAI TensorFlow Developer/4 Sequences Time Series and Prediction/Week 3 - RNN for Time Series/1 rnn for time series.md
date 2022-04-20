<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>


## RNN for Time Series <hr>
RNN is better when using Sequence Data.
Time Series need you to have a cell to maintain data. Data closer to predictive date, has bigger impact right.

Accross long series context, it would be large impact. Financial data, closing price have bigger impact rather tahnn 60 days ago.

We will see `Lambda Layers`, We write for pre and post, NN does the magifc, but we dont have the control. So, lamda allows to have artitari code as a layer.

We'll apply NN and LCM and implement Lambda Layers.

## RNN
Sequentiall process sequences of pinput. 

It could use to predict text, now we use time series.

We can feed batch of sequences, 
input shape [batch_size, timesteps, dims]

For series, things that are closer to the predictive, might have a batter impact rather than those who further away from our target value.

### RNN Shape of Input
If we have a window of 30 timestamps, and we batch them in sizes of 4, the shape will be 4 * 30 * 1

### Sequence to Sequence RNN
Have a batch of sequence, and return a batch of sequence. 

### Lamda Layers
Basically anonymous function, with the power to alter data.
`Huber` Loss function : Good for noisy data.

### Improving with LSTM
