<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>


## Sequences and Prediction <hr>
Sequences data that are changed overtime.

## Time Series <hr>
Different Type of Time Series.
Preparing time series, like splitting data.

Time Series are everyhere. It can be on weather forecast, stock prices.

Time Series : Ordered Sequenced of values, that are equally spaced overtime. 

For example, Univariate Time Series : Single value at each time step. 
You may also encounter time series that have multiple values. Like first values, and second values, in the given time. That's Multivariate.

Multivariate can help you understand impact of related data. 

Anything with a `Time` factor in it, can be analyzed this way. 

What to do with it? We can forecast it, to predict to the future, or the past (imputation). We can also fill the hole in some data. 

### Time Series Patterns
- Trend : See where time series is moving
- Seasonality : Pattern repeats at a predictable interval
- Combination : Some may have combination between it.
- Noise : There are some that are not predictable at all (nothing to do).
- Auto-correlated Time Series : it corellated with a delayed copy of itself called lag. Time series like this describe as having `memory`, as steps are dependent on previous one. The spikes (unpredictable) are `innovations`

Non-stationary Time Series : Sudden distruptives event changes the trend to being unknown. 
To predict it, we could train it for the last 100 steps. 

