<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Train Validate Test <hr>
We divide it into period of each corresponding data (fixed partitioning)

If the data contains seasonality, we want to ensure each period containes whole number of seasons.

first, train with training period. Then validate it using valudation period. Then train it again with testing data, because thesting data are the closest to the current data. and as such it's often the stongest signal in determining future values. 

There's other methodology where test period is the future data. `fixed partitioning` 

Then.. There's ANOTHER method `roll-forward partitioning`, where we start with short training period, and gradually increase it. Say one day at a time, or week. 

