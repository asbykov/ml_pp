# ml_pp
ML/DS Case. Political parties

===============
UPD:
How to run analysis
> jupyter notebook

Choose analysis.ipynb to see the case solution. Dimensionality reduction method is put into separate poly.py module.

To run integration test run the following command
> pytest

The solution was not put into docker container due to lack of time. Integration and unit tests are also not in the best shape for the same reason but the integration test is doing what it is supposed to do
================

Answers to 

5.:

> In the 2D space, paint the area that is valid based on the value bounds of the high dimensional space. I.e., a point that is within the bounds in the high dimensional space must be located inside the painted area in the 2D space.

In my humble opinion, that does not make sense for PCA. We take 43 columns\features and reduce them to 2 features, meaning we take 43-dim space and map it to 2-dim space, in that case it is not one-to-one mapping, the multiplication matrices used in scaling and PCA transformations would every time be different based on the difference in values of the original high-dim space and depending on the difference of values in features, the matrices and mapping would be different as well (every number in every feature might be converted differently depending on what the mean is). Certain features might "get lost" depending on how important they are thus we can not directly say what the boundary would be for that in 2-dim space. Even though the shape of the values on that space will always be somewhat the same (the V-shape), everytime a different set of features might be used to create the mapping and these features could have their own boundaries.

A: 
> Justify your methodological choices in each step (1–5). What other choices could you have made? What would have been their pros and cons?

(in jupyter notebook)

B: 
> Explain in a non-technical way what the low-dimensional representation of the data means (your visualization in the step 2). What could you teach a politician about the European political landscape based on the dimensionality reduction and/or possible additional analyses you may produce?

The visualisation more or less teaches us what we already know (just with pseudo-hard data), it also shows us the probable bias political scientists have on the analysis of political parties and their programmes and view. Even though the questionaire is well-constucted by political science standards, it still can not find something new we did not know before -- it more or less maps all parties on the economic right\left and libertarian\authoritarian 2-D space, a textbook representation of political parties. 

If we reduce parties' views to only 2 dimensions, we more or less always will see a scale on economic left/right or a scale that resembles and correlates with it a lot (0.32 variance in my case out of 1.0) -- we can see that if we color-code parties with economic "extreme" views: more than one standard deviation from the mean -- surprisingly, economic left parties are on the left of the plot and economic right on the right, this is due to 1) economic policy IS the most important difference between political parties 2) economic left values were usually represented by "lower" scores (0,1,2). And in that case the second dimension (0.15 variance) somewhat resemples libertarian\authoritarian scale (but not really, although it does correlate a lot). These two plots give us the classic libertarian-left / centrists / authoritarian-right clusters were political parties align within these clusters with only a few outliers. Whatever the 2 scales are, extreme-right and extreme-left will always stay close to one another and I think that shows bias in the questions asked.

--

What could that teach a European politican? Probably not much if he or she is already savvy in political science. Maybe that these two scales are the most important, of course, but they do not cover even the 0.5 variance (combined) in the political landscape of the European parties. Political parties are not only the dot on the 2-D scale, even though that dot explains how they would react and what they would say probably 50% of the time. Also if you keep asking questions that are a substitution for a classic 2-D scale, you will always get that same scale in the end no matter how you interpret the results. It's a self-replecating loop.

C:
> How would you deploy the model to a cloud environment so that it would be able to withstand 1 million users per hour? You can for example include a sketch of a cloud architecture.

1 million users per hour is roughly 300 users per second. That is a lot, but not extremely much. Considering the situation that we need a model in the cloud that would predict position of a "new" party in a 2D space every time based on the same 43 features, I think any serverless solution would be good enough both in terms of deployments' complexity and costs. For simplicity let's consider lambda functions (AWS) as a core instrument -- we put model weights, scaler, PCA-transformer in S3 bucket (simple storage that can be called several times a second without delays), when lambda function starts, it downloads everything we need for analysing into RAM. In that case, I think, every lambda needs no more than a half second to prepare everything for analysing. We setup lambda functions to accept api calls, kafka streams or whatever is necessary to process the loads, while AWS handles load-balancing and horizontal scaling for lambda functions for us. 

In that case we can handle both peak loads (but not hard-hard peak loads) and at the same time idling would not be an issue during non-peak periods. The analysis itself is not much of the hassle in computing costs -- only a few matrices to multiply in the end where no matrix is bigger than 100x100. 

It's not clear, though, what is the end destination for our deployment, let's for simplicity assume it's the database -- for that I would use Dynamodb as it is perfect for "indefinite" filling up with similar data with flat structure. It's hard to say something more for an abstract case like that but nothing extremely complex should be necessary.
