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

# 7. Sampling & Sampling Distribution
## 7.1 Point Estimators
![Slide](assets/PL07-Sampling-SamplingDistribution/PointEstimator/1.png) 
![Slide](assets/PL07-Sampling-SamplingDistribution/PointEstimator/2.png) 
![Slide](assets/PL07-Sampling-SamplingDistribution/PointEstimator/3.png) 
![Slide](assets/PL07-Sampling-SamplingDistribution/PointEstimator/4.png) 
![Slide](assets/PL07-Sampling-SamplingDistribution/PointEstimator/5.png) 
![Slide](assets/PL07-Sampling-SamplingDistribution/PointEstimator/6.png) 
## 7.2 Sample Distributions
![Slide](assets/PL07-Sampling-SamplingDistribution/SamplingDistribution/1.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SamplingDistribution/2.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SamplingDistribution/3.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SamplingDistribution/4.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SamplingDistribution/5.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SamplingDistribution/6.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SamplingDistribution/7.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SamplingDistribution/8.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SamplingDistribution/9.png)
## 7.3 Standard Error of the Mean
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/1.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/2.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/3.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/4.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/5.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/6.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/7.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/8.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/9.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/10.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/11.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/12.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/13.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/14.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/15.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/StandardErrorOfTheMean/16.png)
## 7.4 Sample Mean Proximity to Population Mean
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/1.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/2.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/3.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/4.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/5.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/6.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/7.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/8.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/9.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/10.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/11.png)
![Slide](assets/PL07-Sampling-SamplingDistribution/SampleMeanProximityToPopMean/12.png)

# 8. Confidence Interval Estimation
## 8.1 Confidence Interval Estimation - Sigma Known
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/1.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/2.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/3.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/4.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/5.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/6.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/7.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/8.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/9.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/10.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/11.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/12.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/13.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/14.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/15.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/16.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation_Sigma_Known/17.png)

## 8.2 Confidence Interval Estimation - Sigma Unknown
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/1.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/2.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/3.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/4.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/5.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/6.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/7.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/8.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/9.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/10.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/11.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceIntervalEstimation-SigmaUnknown/12.png)

## 8.4 Confidence Interval - Examples - Samples Needed
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/1.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/2.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/3.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/4.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/5.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/6.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/7.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/8.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/9.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/10.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/11.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/12.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/13.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/14.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/15.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/16.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/17.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/18.png)
![Slide](assets/PL08-Confidence_Interval_Estimation/ConfidenceInterval-Example-SamplesNeeded/19.png)

# 9. Hypothesis Formulation
## 9.1 Introduction to Hypothesis
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/8.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/9.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/10.png)
![Slide](assets/PL09-Hypothesis-Formulation/Intro-Hypothesis/11.png)

## 9.2 Null and Alternative Hypotheses
![Slide](assets/PL09-Hypothesis-Formulation/NullVSAlternative/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/NullVSAlternative/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/NullVSAlternative/3.png)

## 9.3 Hypothesis Examples
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/8.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/9.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/10.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/11.png)
![Slide](assets/PL09-Hypothesis-Formulation/HypothesisExamples/12.png)

## 9.4 Type I & Type II Errors
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/8.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/9.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/10.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIErrors/11.png)

## 9.5 Type I & Type II Examples
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIExamples/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIExamples/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIExamples/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIExamples/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIExamples/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIExamples/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIExamples/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/TypeITypeIIExamples/8.png)

## 9.6 Visualize Type I & Type II Errors
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/8.png)
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/9.png)
![Slide](assets/PL09-Hypothesis-Formulation/VisualizeTypeITypeIIErrors/10.png)

## 9.7 Single Sample Hypothesis Z-test
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test/8.png)

## 9.8 Single Sample Hypothesis Z-test Examples
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/8.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/9.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-test-Examples/10.png)

## 9.9 Single Sample Hypothesis Z-test Alpha & P-Values
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-testAlpha_PValues/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-testAlpha_PValues/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesisZ-testAlpha_PValues/3.png)

## 9.10 Single Sample Hypothesis t-test
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test/7.png)

## 9.11 Single Sample Hypothesis t-test Examples
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/8.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/9.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/10.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/11.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/12.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/13.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/14.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/15.png)
![Slide](assets/PL09-Hypothesis-Formulation/SingleSampleHypothesist-test-Examples/16.png)

## 9.12 Calculate Type II Errors
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/8.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/9.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/10.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/11.png)
![Slide](assets/PL09-Hypothesis-Formulation/Calculate_TypeII_Errors/12.png)

## 9.13 Test Power Curve
![Slide](assets/PL09-Hypothesis-Formulation/TestPowerCurve/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/TestPowerCurve/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/TestPowerCurve/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/TestPowerCurve/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/TestPowerCurve/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/TestPowerCurve/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/TestPowerCurve/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/TestPowerCurve/8.png)

## 9.14 Controlling Type II Errors Using Sample Size
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/1.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/2.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/3.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/4.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/5.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/6.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/7.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/8.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/9.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/10.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/11.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/12.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/13.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/14.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/15.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/16.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/17.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/18.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/19.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/20.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/21.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/22.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/23.png)
![Slide](assets/PL09-Hypothesis-Formulation/CalculatingTypeIIExamples/24.png)

# 10. PL10 Z-tests T-tests for Two Populations
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/1.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/2.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/3.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/4.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/5.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/6.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/7.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/8.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/9.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/10.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/11.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/12.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Z-TestForTwoPops/13.png)

## 10.2 Two Populations T-Test Hypothesis
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/1.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/2.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/3.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/4.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/5.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/6.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/7.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/8.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/9.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/10.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/11.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/12.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/13.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/14.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/15.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/16.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/17.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/18.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/Two_Populations_T-Test_Hypothesis/19.png)

## 10.3 Two Populations, Matched Sample t-test
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/1.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/2.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/3.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/4.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/5.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/6.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/7.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/8.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/9.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/10.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/11.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/12.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/13.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/14.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/15.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/16.png)
![Slide](assets/PL10_Z-tests_T-tests_for_Two_Populations/TwoPopulations_Matched_Sample_t-test/17.png)

# 11 PL11 Inferences about Population Variances
## 11.1 Variance and its Sampling Distribution
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/1.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/2.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/3.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/4.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/5.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/6.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/7.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/8.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/9.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/10.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/11.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/12.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/13.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/14.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/15.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/16.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/17.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/18.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/1-Variance_and_its_Sampling_Distribution/19.png)

## 11.2 Confidence Intervals for the Variance
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/1.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/2.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/3.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/4.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/5.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/6.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/7.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/8.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/9.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/10.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/11.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/12.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/13.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/14.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/15.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/16.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/17.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/18.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/19.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/2-Confidence_Intervals_for_the_Variance/20.png)

## 11.3 Hypothesis Tests for the Variance
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/1.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/2.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/3.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/4.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/5.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/6.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/7.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/8.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/9.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/10.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/11.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/12.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/13.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/14.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/15.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/16.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/3-Hypothesis_Tests_forthe_Variance/17.png)

## 11.4 F-Ratio Test for Two Equal Variances
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/1.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/2.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/3.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/4.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/5.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/6.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/7.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/8.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/9.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/10.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/11.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/4-F-ratioTestforTwoEqualVariances/12.png)

## 11.5 F-Ratio Test Practice for Two Equal Variances
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/1.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/2.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/3.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/4.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/5.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/6.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/7.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/8.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/9.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/10.png)
![Slide](assets/PL11-Inferences_about_Population_Variances/5-F-ratio_Test_PRACTICE/11.png)

# 12 Statistics PL12 - Goodness of Fit and Independence 
## 12.1 Introduction to the Chi-square Test
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/1.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/2.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/3.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/4.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/5.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/6.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/7.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/8.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/9.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/10.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/11.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/12.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/13.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/14.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/15.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/16.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/17.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/18.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/19.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/20.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/21.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/22.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/1-Introduction-Chi-squareTest/23.png)

## 12.2 Chi-square in Excel using College Enrollment Data
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/1.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/2.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/3.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/4.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/5.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/6.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/7.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/8.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/9.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/10.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/11.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/12.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/13.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/14.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/15.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/16.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/17.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/18.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/19.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/20.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/21.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/22.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/23.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/24.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/25.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/26.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/27.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/28.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/29.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/30.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/31.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/32.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/33.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/34.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/35.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/36.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/37.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/38.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/39.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/40.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/41.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/42.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/43.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/44.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/45.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/46.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/47.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/48.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/49.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/50.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/51.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/52.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/53.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/54.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/55.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/56.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/57.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/58.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/59.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/60.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/2-Chi-square-in-Excel-using-College-Enrollment-Data/61.png)

## 12.3 Chi-Square in SPSS
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/1.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/2.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/3.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/4.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/5.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/6.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/7.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/8.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/9.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/10.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/11.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/12.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/13.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/14.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/15.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/16.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/17.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/18.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/19.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/20.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/21.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/22.png)
![Slide](assets/PL12-Goodness_of_Fit_and_Independence_Tests/3-Chi-Square-SPSS/23.png)

# 13 - ANOVA
## 13.1 ANOVA - A Visual Introduction
![Slide](assets/PL13-ANOVA/1-Intro/1.png)
![Slide](assets/PL13-ANOVA/1-Intro/2.png)
![Slide](assets/PL13-ANOVA/1-Intro/3.png)
![Slide](assets/PL13-ANOVA/1-Intro/4.png)
![Slide](assets/PL13-ANOVA/1-Intro/5.png)
![Slide](assets/PL13-ANOVA/1-Intro/6.png)
![Slide](assets/PL13-ANOVA/1-Intro/7.png)
![Slide](assets/PL13-ANOVA/1-Intro/8.png)
![Slide](assets/PL13-ANOVA/1-Intro/9.png)
![Slide](assets/PL13-ANOVA/1-Intro/10.png)
![Slide](assets/PL13-ANOVA/1-Intro/11.png)
![Slide](assets/PL13-ANOVA/1-Intro/12.png)
![Slide](assets/PL13-ANOVA/1-Intro/13.png)
![Slide](assets/PL13-ANOVA/1-Intro/14.png)