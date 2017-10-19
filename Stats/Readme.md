## Statistics Review
##### Notes from Youtube video created by [Brandon Foltz](https://www.youtube.com/channel/UCFrjdcImgcQVyFbK04MBEhA)
# 1. Population VS Sample Data
[video](https://www.youtube.com/watch?v=8X2xfwBP4uo&list=PLAshlHpA2Iwc10-3HIioqUtqG0Fc4MNpp&index=1&t=207s)
![Slide](assets/Slide1.png)

1. Not all the bulbs have the same longevity and power consumption -> they have some __*variation*__ (__standard deviation__) in both longevity and power consumption.
2. How do you test the whole *population* of bulbs wheter they conform to industry standard? You need *sample* of the *entire* population.

![Slide 2](assets/Slide2.png)

1. If you collect data on the WHOLE populatoin, it's called *census*.

![Slide 3](assets/Slide3.png)

1. Sample must be "__well-chosen__". But how?
2. Sample should be "__independent__" of each other.
3. Random sample is mostly used.

![Slide 4](assets/Slide4.png)

* You can't include 'men', 'women from other countries', 'older than 35 or younger than 18 female'.
* If half of you sample is NBA female, then they do not representn the whole population (NBA players are much taller than average).
* Like friend chooses friends to form a sample group (as they are like-minded).
* Say you call landline to collect interview data, but people mostly use mobile now. So people you got from landline interview does not necessarily represent the whole population.

![Slide 5](assets/Slide5.png)

![Slide 6](assets/Slide6.png)
A *sample* is an __approximation__ of the *population*.
* so always uncentainty attached to that approximation.

![Slide 7](assets/Slide7.png)

# Measure of Varibility:
## Variance & Standard Deviation
##### When you take sample out of the whole population, you will have errors or uncertainty => *variability*
We'll measure it -> variance & SD.

![Slide 8](assets/Slide8.png)
![Slide 9](assets/Slide9.png)
* Same *__mean__* doesn't tell anythin.
* Look at how data points show **spread** (or *distribution* or *variability*)
* Both classes have the same *mean* but Class1 has greater *variability* (or more spread out).
* Students in Class2 are more consistent to the scores (closer to the *mean*).

![Slide 10](assets/Slide10.png)
* Variance & SD help us answer -> how far datapoints are from the mean.
* Variance & SD are lower if spread less (see green stars vs blue stars above).
* Mean, Variance, SD should be used to compare against each other or against theoretical values.

![Slide 11](assets/Slide11.png)
![Slide 12](assets/Slide12.png)
![Slide 13](assets/Slide13.png)
![Slide 14](assets/Slide14.png)
![Slide 15](assets/Slide15.png)
![Slide 16](assets/Slide16.png)
* SD = sum of (diffences)


### Example - 2010 & 2011 NFL Goal Kick Data
The [excel](assets/nfl.xlsx) and [numbers (Mac)](assets/nfl.numbers) files are included.
* note that the [database obtained](http://www.nfl.com/stats/categorystats?seasonType=REG&d-447263-n=1&d-447263-o=2&d-447263-p=1&d-447263-s=KICKING_FG_LONG&tabSeq=0&season=2010&Submit=Go&experience=&archive=true&statisticCategory=FIELD_GOALS&conference=null&qualified=false) for this is different from the one shown in the original clips. Numbers (Number of datasets, Mean, Variance, and Standard Deviation) are a little bit different. 

Below are the screenshots of 2010 and 2011 field goals.
In this example we're interested in 'Line of Scrimmage' for the coach to analyze the distance for his or her kickers.

'Scrimmage' = 'Lng' - 17 yards.
</br>
'Placement' = 'Lng' - 7 Yards.

![Slide 17](assets/Slide17.png)
![Slide 18](assets/Slide18.png)
![Slide 20](assets/Slide20.png)
![Slide 21](assets/Slide21.png)
![Slide 19](assets/Slide19.png)

Notice the bell shape (histogram), the higher the SD, the more spread of the bell shape.

## Understand Z-Score
### Measures of Variability
Z-Score is a measurement of variability (how far is that datapoint from the mean) in multiplication of SD.

</br>
So, the mean itself has z-score of 0.
You would get a distance (z-score) by finding the distance from datapoint to the mean (x - x-bar) divided by SD.

![Slide 22](assets/Slide22.png)
![Slide 23](assets/Slide23.png)
![Slide 24](assets/Slide24.png)
![Slide 25](assets/Slide25.png)
![Slide 26](assets/Slide26.png)
![Slide 27](assets/Slide27.png)

# 2. Normal Distribution
### Is my data normal?
#### Before getting into stats calcs, we should visually see the data first.
##### Because some if not most calcs assume your data to be normally distributed.

![Slide 29](assets/Slide29.png)

These are visual tools to help you see data graphially.
![Slide 30](assets/Slide30.png)

![Slide 31](assets/Slide31.png)
![Slide 32](assets/Slide32.png)
![Slide 33](assets/Slide33.png)
![Slide 34](assets/Slide34.png)
![Slide 35](assets/Slide35.png)
![Slide 36](assets/Slide36.png)
For example, at the frequency of 5.0, Stem of 2 --> Each data point => Stem x Stem witdh 'Joined By' Leaf
</br>
0.021, 0.023, 0.023, 0.023, and 0.024
![Slide 37](assets/Slide37.png)
Box plots can also tell you if your data is normal if:
* it looks symmetrical.
* Quartile 1 & Quartile 3 are pretty much the same distance from the __median__ (datapoint in the middle).
* Top and bottom whiskers (vertical lines) are pretty much same length.

Note that 5 data points on above top whisker and 4 points below bottom whisker are data points that *__1.5 interquartile ranges__*.

![Slide 38](assets/Slide38.png)
![Slide 39](assets/Slide39.png)

#### Example - Is this data set normal?

![Slide 40](assets/Slide40.png)
![Slide 41](assets/Slide41.png)
![Slide 42](assets/Slide42.png)
So it does not fit normal distribution.
(Fits Lognormal)
 # 3. Bivariate Relationship
 ## 3.1 Covariance
 Looking at linear relationship between the 2 variables. *How they behave in PAIR.*
 These are loosely related:
 - Covariance
 - Linear Regression
 - Correlation

*__Covariance Example__*: Relationship between S&P VS. Dow Jones monthly return in 2012.
* At time '1' S&P return of 3.97% vs Dow Jones of 2.49%.
* If 'var A' moves this much, how would the 'var B' behave?
* It has 'LINEAR' pattern.
* If SP500 increases, DJI will also increase.
* This represent the reality that both of these indexes measure the same thing -- overall performance of stock market (but different ways).
![Slide 43](assets/Slide43.png)
![Slide 44](assets/Slide44.png)

#### Covariance is about DIRECTION only.
not strength.
</br>
'+' -> One goes up, the other goes up.
'-' -> One goes up, the other goes down.
'0' -> No pattern.
![Slide 45](assets/Slide45.png)
![Slide 46](assets/Slide46.png)
![Slide 47](assets/Slide47.png)

#### Formulas
Summation of (Each data point subtracts its mean) Times (Each data point subtracts its mean)
Divided by n - 1 or N __depending upon sample or population__
![Slide 48](assets/Slide48.png)

#### Example
![Slide 49](assets/Slide49.png)
![Slide 50](assets/Slide50.png)
![Slide 51](assets/Slide51.png)
![Slide 52](assets/Slide52.png)
![Slide 53](assets/Slide53.png)
![Slide 54](assets/Slide54.png)
* Take a sample of 10 data points collected each hours for number of workers (x) on the floor VS. number of product made (y) per that hour.
* We can calc that Covariance is POSITIVE 106.93 which means more workers more products, less workers less products.
* In Covariance, we only interested in 'POSITIVE' direction (sign) not the value of 106.93.

## 3.2 Covariance Matrix
Example: We have 4 variabes with number of sample of 20. Output from SPSS as follows:
![Slide 55](assets/Slide55.png)
* First thing we should do is VISUALLY INSPECT it wheter we might or might not have a linear relationship between what and what.
*__DUPLICATES__** means upper and lower diagonal are the same.
![Slide 56](assets/Slide56.png)
* Diagonals are **VARIANCE.**
![Slide 57](assets/Slide57.png)
![Slide 58](assets/Slide58.png)
* Covariance between the 2 variables are shown.
![Slide 59](assets/Slide59.png)

## 3.3 Correlation
- Same as Covariance but has 'Strength' indicator on top of 'Direction'.
- Correlation is between -1 and +1. So you can compare variables with different units.
- Correlation is standardized. Like z-score which measures how far that data point is from the mean (remember mean itself is 0).
![Slide 60](assets/Slide60.png)

*__What to look for__*
![Slide 61](assets/Slide61.png)
- VISUALLY LOOK AT SCATTER PLOT FIRST.
- Correlation is for LINEAR ONLY.
- Correlation might show up for some not-making sense stuff. Like full moon and number of dog barks.
- Watch out for correlation strength.

![Slide 62](assets/Slide62.png)
![Slide 63](assets/Slide63.png)
#### Example
SPSS output for DJI vs SP500 -> Correlation = 0.974
- DIAGONALS = Correlation
![Slide 64](assets/Slide64.png)
![Slide 65](assets/Slide65.png)
#### Example
![Slide 66](assets/Slide66.png)
![Slide 67](assets/Slide67.png)
![Slide 68](assets/Slide68.png)
![Slide 69](assets/Slide69.png)
![Slide 70](assets/Slide70.png)
![Slide 71](assets/Slide71.png)

# 4. Permutations VS. Combinations
![Slide 72](assets/Slide72.png)
![Slide 73](assets/Slide73.png)
![Slide 74](assets/Slide74.png)
![Slide 75](assets/Slide75.png)
![Slide 76](assets/Slide76.png)
![Slide 77](assets/Slide77.png)
 
## 4.1 Combinations
### Order doesn't matter
![Slide 78](assets/Combination.png)
![Slide 79](assets/Combination1.png)
![Slide 80](assets/Combination2.png)
## 4.2 Permutations
### Order matters
![Slide 81](assets/Permutation.png)
![Slide 82](assets/Permutation1.png)
![Slide 83](assets/Permutation2.png) 

## 4.3 Examples of Combinations
### Losing Marbles
![Slide](assets/LosingMarble/LosingMarble1.png)
![Slide](assets/LosingMarble/LosingMarble2.png)
![Slide](assets/LosingMarble/LosingMarble3.png)
![Slide](assets/LosingMarble/LosingMarble4.png)
![Slide](assets/LosingMarble/LosingMarble5.png)
![Slide](assets/LosingMarble/LosingMarble6.png)
![Slide](assets/LosingMarble/LosingMarble7.png)
![Slide](assets/LosingMarble/LosingMarble8.png)
![Slide](assets/LosingMarble/LosingMarble9.png)
### Dogs of the Dow
![Slide](assets/DogsOfTheDow/DogsOfTheDow1.png)
![Slide](assets/DogsOfTheDow/DogsOfTheDow2.png)
![Slide](assets/DogsOfTheDow/DogsOfTheDow3.png)
![Slide](assets/DogsOfTheDow/DogsOfTheDow4.png)
![Slide](assets/DogsOfTheDow/DogsOfTheDow5.png)
![Slide](assets/DogsOfTheDow/DogsOfTheDow6.png)
![Slide](assets/DogsOfTheDow/DogsOfTheDow7.png)
![Slide](assets/DogsOfTheDow/DogsOfTheDow8.png)
![Slide](assets/DogsOfTheDow/DogsOfTheDow9.png)
### Nearly Normal
![Slide](assets/NearlyNormal/NearlyNormal1.png)
![Slide](assets/NearlyNormal/NearlyNormal2.png)
![Slide](assets/NearlyNormal/NearlyNormal3.png)
![Slide](assets/NearlyNormal/NearlyNormal4.png)
![Slide](assets/NearlyNormal/NearlyNormal5.png)
![Slide](assets/NearlyNormal/NearlyNormal6.png)
![Slide](assets/NearlyNormal/NearlyNormal7.png)
### Under The Curve
![Slide](assets/UnderTheCurve/UnderTheCurve1.png)
![Slide](assets/UnderTheCurve/UnderTheCurve2.png)
![Slide](assets/UnderTheCurve/UnderTheCurve3.png)
![Slide](assets/UnderTheCurve/UnderTheCurve4.png)
![Slide](assets/UnderTheCurve/UnderTheCurve5.png)
![Slide](assets/UnderTheCurve/UnderTheCurve6.png)
![Slide](assets/UnderTheCurve/UnderTheCurve7.png)
![Slide](assets/UnderTheCurve/UnderTheCurve8.png)
![Slide](assets/UnderTheCurve/UnderTheCurve9.png)
![Slide](assets/UnderTheCurve/UnderTheCurve10.png)
![Slide](assets/UnderTheCurve/UnderTheCurve11.png)

## 4.4 Finite Math: Set Operations and Notation
![Slide](assets/Sets/Set1.png)
![Slide](assets/Sets/Set2.png)
![Slide](assets/Sets/Set3.png)
![Slide](assets/Sets/Set4.png)
![Slide](assets/Sets/Set5.png)
![Slide](assets/Sets/Set6.png)
![Slide](assets/Sets/Set7.png)
![Slide](assets/Sets/Set8.png)
![Slide](assets/Sets/Set9.png)
![Slide](assets/Sets/Set10.png)

## 4.5 Venn Diagram Basics
![Slide](assets/VennDiagramBasic/VennDiagramBasic1.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic2.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic3.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic4.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic5.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic6.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic7.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic8.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic9.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic10.png)
![Slide](assets/VennDiagramBasic/VennDiagramBasic11.png)

## 4.6 Venn Diagram Region
![Slide](assets/VennDiagramRegion/VennDiagramRegion1.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion2.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion3.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion4.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion5.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion6.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion7.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion8.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion9.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion10.png)
![Slide](assets/VennDiagramRegion/VennDiagramRegion11.png)

## 4.7 Venn Diagram Practice
![Slide](assets/VennPractice/VennPractice1.png)
![Slide](assets/VennPractice/VennPractice2.png)
![Slide](assets/VennPractice/VennPractice3.png)
![Slide](assets/VennPractice/VennPractice4.png)
![Slide](assets/VennPractice/VennPractice5.png)
![Slide](assets/VennPractice/VennPractice6.png)

## 4.8 Joint & Marginal Probability
![Slide](assets/JointMarginalProb/JointMarginalProb1.png)
![Slide](assets/JointMarginalProb/JointMarginalProb2.png)
![Slide](assets/JointMarginalProb/JointMarginalProb3.png)
![Slide](assets/JointMarginalProb/JointMarginalProb4.png)
![Slide](assets/JointMarginalProb/JointMarginalProb5.png)
![Slide](assets/JointMarginalProb/JointMarginalProb6.png)
![Slide](assets/JointMarginalProb/JointMarginalProb7.png)
![Slide](assets/JointMarginalProb/JointMarginalProb8.png)
![Slide](assets/JointMarginalProb/JointMarginalProb9.png)

## 4.9 Playing With Full Deck (Combination Example)
![Slide](assets/PlayingFullDeck/PlayingFullDeck1.png)
![Slide](assets/PlayingFullDeck/PlayingFullDeck2.png)
![Slide](assets/PlayingFullDeck/PlayingFullDeck3.png)
![Slide](assets/PlayingFullDeck/PlayingFullDeck4.png)
![Slide](assets/PlayingFullDeck/PlayingFullDeck5.png)
![Slide](assets/PlayingFullDeck/PlayingFullDeck6.png)

# 5. Discrete Probability Distributions (PL05)
## 5.1 Random Variable Basics
![Slide](assets/RandomVariableBasic/RandomVariableBasic1.png)
![Slide](assets/RandomVariableBasic/RandomVariableBasic2.png)
![Slide](assets/RandomVariableBasic/RandomVariableBasic3.png)
![Slide](assets/RandomVariableBasic/RandomVariableBasic4.png)
![Slide](assets/RandomVariableBasic/RandomVariableBasic5.png)
![Slide](assets/RandomVariableBasic/RandomVariableBasic6.png)

## 5.2 Discrete Random Variable Basics
![Slide](assets/DiscreteRandomVariable/DiscreteRandomVariable1.png)
![Slide](assets/DiscreteRandomVariable/DiscreteRandomVariable2.png)
![Slide](assets/DiscreteRandomVariable/DiscreteRandomVariable3.png)
![Slide](assets/DiscreteRandomVariable/DiscreteRandomVariable4.png)
![Slide](assets/DiscreteRandomVariable/DiscreteRandomVariable5.png)

## 5.3 Discrete Random Variable Probability
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb1.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb2.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb3.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb4.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb5.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb6.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb7.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb8.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb9.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb10.png)
![Slide](assets/DiscreteRandomVariableProb/DiscreteRandomVariableProb11.png)

## 5.4 Expected Value
![Slide](assets/ExpectedValue/ExpectedValue1.png)
![Slide](assets/ExpectedValue/ExpectedValue2.png)
![Slide](assets/ExpectedValue/ExpectedValue3.png)
![Slide](assets/ExpectedValue/ExpectedValue4.png)
![Slide](assets/ExpectedValue/ExpectedValue5.png)
![Slide](assets/ExpectedValue/ExpectedValue6.png)
![Slide](assets/ExpectedValue/ExpectedValue7.png)
![Slide](assets/ExpectedValue/ExpectedValue8.png)
![Slide](assets/ExpectedValue/ExpectedValue9.png)
![Slide](assets/ExpectedValue/ExpectedValue10.png)
![Slide](assets/ExpectedValue/ExpectedValue11.png)
![Slide](assets/ExpectedValue/ExpectedValue12.png)
![Slide](assets/ExpectedValue/ExpectedValue13.png)

## 5.5 Discrete Random Variance
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance1.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance2.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance3.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance4.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance5.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance6.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance7.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance8.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance9.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance10.png)
![Slide](assets/DiscreteRandomVarVariance/DiscreteRandomVarVariance11.png)

## 5.6 Binomial Distribution
![Slide](assets/BinomialDistribution/BinomialDistribution1.png)
![Slide](assets/BinomialDistribution/BinomialDistribution2.png)
![Slide](assets/BinomialDistribution/BinomialDistribution3.png)
![Slide](assets/BinomialDistribution/BinomialDistribution4.png)
![Slide](assets/BinomialDistribution/BinomialDistribution5.png)
![Slide](assets/BinomialDistribution/BinomialDistribution6.png)
![Slide](assets/BinomialDistribution/BinomialDistribution7.png)
![Slide](assets/BinomialDistribution/BinomialDistribution8.png)
![Slide](assets/BinomialDistribution/BinomialDistribution9.png)
![Slide](assets/BinomialDistribution/BinomialDistribution10.png)
![Slide](assets/BinomialDistribution/BinomialDistribution11.png)
![Slide](assets/BinomialDistribution/BinomialDistribution12.png)
![Slide](assets/BinomialDistribution/BinomialDistribution13.png)
![Slide](assets/BinomialDistribution/BinomialDistribution14.png)
![Slide](assets/BinomialDistribution/BinomialDistribution15.png)
![Slide](assets/BinomialDistribution/BinomialDistribution16.png)
![Slide](assets/BinomialDistribution/BinomialDistribution17.png)

## 5.7 Binomial Mean & Standard Deviation
![Slide](aseets/BinomailMeanSD/BinomailMeanSD1.png)
![Slide](aseets/BinomailMeanSD/BinomailMeanSD2.png)
![Slide](aseets/BinomailMeanSD/BinomailMeanSD3.png)
![Slide](aseets/BinomailMeanSD/BinomailMeanSD4.png)
![Slide](aseets/BinomailMeanSD/BinomailMeanSD5.png)
![Slide](aseets/BinomailMeanSD/BinomailMeanSD6.png)
![Slide](aseets/BinomailMeanSD/BinomailMeanSD7.png)
![Slide](aseets/BinomailMeanSD/BinomailMeanSD8.png)
![Slide](aseets/BinomailMeanSD/BinomailMeanSD9.png)

## 5.8 Binomial Example - Sales Problem
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales1.png)
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales2.png)
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales3.png)
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales4.png)
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales5.png)
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales6.png)
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales7.png)
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales8.png)
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales9.png)
![Slide](assets/BinomialExample_Sales/BinomialExample_Sales10.png)

## 5.9 Binomial Example - Mac OSX Users
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac1.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac2.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac3.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac4.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac5.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac6.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac7.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac8.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac9.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac10.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac11.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac12.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac13.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac14.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac15.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac16.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac17.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac18.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac19.png)
![Slide](assets/BinomialExample_Mac/BinomialExample_Mac20.png)

## 5.10 Binomial Example - Accident in Factory
![Slide](assets/BinomialExample_Accident/BinomialExample_Accident1.png)
![Slide](assets/BinomialExample_Accident/BinomialExample_Accident2.png)
![Slide](assets/BinomialExample_Accident/BinomialExample_Accident3.png)
![Slide](assets/BinomialExample_Accident/BinomialExample_Accident4.png)
![Slide](assets/BinomialExample_Accident/BinomialExample_Accident5.png)
![Slide](assets/BinomialExample_Accident/BinomialExample_Accident6.png)
![Slide](assets/BinomialExample_Accident/BinomialExample_Accident7.png)
![Slide](assets/BinomialExample_Accident/BinomialExample_Accident8.png)

## 5.11 Poisson Distribution
![Slide](assets/PoissonDistribution/PoissonDistribution1.png)
![Slide](assets/PoissonDistribution/PoissonDistribution2.png)
![Slide](assets/PoissonDistribution/PoissonDistribution3.png)
![Slide](assets/PoissonDistribution/PoissonDistribution4.png)
![Slide](assets/PoissonDistribution/PoissonDistribution5.png)
![Slide](assets/PoissonDistribution/PoissonDistribution6.png)
![Slide](assets/PoissonDistribution/PoissonDistribution7.png)
![Slide](assets/PoissonDistribution/PoissonDistribution8.png)
![Slide](assets/PoissonDistribution/PoissonDistribution9.png)
![Slide](assets/PoissonDistribution/PoissonDistribution10.png)
![Slide](assets/PoissonDistribution/PoissonDistribution11.png)
![Slide](assets/PoissonDistribution/PoissonDistribution12.png)
![Slide](assets/PoissonDistribution/PoissonDistribution13.png)

## 5.12 Poisson Example - Bank & Deer
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer1.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer2.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer3.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer4.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer5.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer6.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer7.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer8.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer9.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer10.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer11.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer12.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer13.png)
![Slide](assets/PoissonExample_BankDeer/PoissonExample_BankDeer14.png)

# 6. Uniform Probability Distribution
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution1.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution2.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution3.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution4.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution5.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution6.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution7.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution8.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution9.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution10.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution11.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution12.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution13.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution14.png)
![Slide](assets/UniformProbabilityDistribution/UniformProbabilityDistribution15.png)

## 6.1 A Tour of Normal Distribution
![Slide](assets/NormalDistribution/NormalDistribution1.png)
![Slide](assets/NormalDistribution/NormalDistribution2.png)
![Slide](assets/NormalDistribution/NormalDistribution3.png)
![Slide](assets/NormalDistribution/NormalDistribution4.png)
![Slide](assets/NormalDistribution/NormalDistribution5.png)
![Slide](assets/NormalDistribution/NormalDistribution6.png)
![Slide](assets/NormalDistribution/NormalDistribution7.png)
![Slide](assets/NormalDistribution/NormalDistribution8.png)
![Slide](assets/NormalDistribution/NormalDistribution9.png)
![Slide](assets/NormalDistribution/NormalDistribution10.png)
![Slide](assets/NormalDistribution/NormalDistribution11.png)
![Slide](assets/NormalDistribution/NormalDistribution12.png)
![Slide](assets/NormalDistribution/NormalDistribution13.png)
![Slide](assets/NormalDistribution/NormalDistribution14.png)
![Slide](assets/NormalDistribution/NormalDistribution15.png)
![Slide](assets/NormalDistribution/NormalDistribution16.png)
![Slide](assets/NormalDistribution/NormalDistribution17.png)

## 6.2 Z or T Distribution?
![Slide](assets/ZorT_Distribution/ZorT_Distribution1.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution2.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution3.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution4.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution5.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution6.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution7.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution8.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution9.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution10.png)
![Slide](assets/ZorT_Distribution/ZorT_Distribution11.png)
 ## 6.3 Normal Distribution Example
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example1.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example2.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example3.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example4.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example5.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example6.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example7.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example8.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example9.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example10.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example11.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example12.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example13.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example14.png)
 ![Slide](assets/NormalDistribution_Example/NormalDistribution_Example15.png)