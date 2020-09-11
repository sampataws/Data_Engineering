##What is Spark Broadcast?
Spark Broadcast variables are secured, read-only variables that get distributed and cached to worker nodes. This is helpful to Spark because when the driver sends packets of information to worker nodes, it sends the data and tasks attached together which could be a little heavier on the network side. Broadcast variables seek to reduce network overhead and to reduce communications. Spark Broadcast variables are used only with Spark Context.


https://github.com/udacity/nd027-c3-data-lakes-with-spark/tree/master/Debugging_And_Optimization