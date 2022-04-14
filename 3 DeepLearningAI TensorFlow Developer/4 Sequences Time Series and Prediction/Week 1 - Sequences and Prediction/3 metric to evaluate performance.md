<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Metrics <hr>
errors = forecasts - actual
mse = np.square(errors).mean()
rmse = np.sqrt(mse)
mae = np.abs(errors).mean()
mape = np.abs(errors / x_valid).mean()

Use MSE if large errors are potentially dangerous and they cost you much more than smaller errors
Use MAE if your gain or your loss is just proportional to the size of the error

`Moving Average`
`Diferencing` : Instead of studying the time series itself, we study the difference between the value at time (t) and the value of an earlier period.

So you can use differencing, then after having the `Moving Average` to it, restore by adding the t value 

Orr, use trailing moving average of ddifference time series + centered moving average of past series (t-365)


