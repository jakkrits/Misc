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


