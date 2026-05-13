# Stump Duty Calculator

In the UK, when you buy a property you pay tax on the purchase of the home called stamp duty.
The amount of tax you pay depends on two factors, the type of buyer you are and the value of the home.

Stamp duty is calculated based on tax bands and each buyer type has their own set of tax bands.
A tax band is represented by a value range that is taxed.

Each tax rate is applied to the value of the property that fits within each band.
The tax rate increases as the taxable amount increases.

For the purposes of this test we will assign the following tax bands:

First time buyer:
```
+----------------+-------------+------------+
| From           | To          | Tax Rate   |
+----------------+-------------+------------+
| £0             | £250,000    | 0%         |
| £250,000       | £600,000    | 5%         |
| £600,000       | £2,000,000  | 8%         |
| £2,000,000     | And Above   | 12%        |
+----------------+-------------+------------+
```

Normal buyer:
```
+----------------+-------------+------------+
| From           | To          | Tax Rate   |
+----------------+-------------+------------+
| £0             | £125,000    | 0%         |
| £125,000       | £250,000    | 2%         |
| £250,000       | £500,000    | 5%         |
| £500,000       | £1,000,000  | 8%         |
| £1,000,000     | £1,500,000  | 10%        |
| £1,500,000     | And Above   | 12%        |
+----------------+-------------+------------+
```

For example for a £2,000,000 normal buyer purchase, the bands work out like this:

```
£0 to £125,000 at 0% = £0
£125,000 to £250,000 at 2% = £2,500
£250,000 to £500,000 at 5% = £12,500
£500,000 to £1,000,000 at 8% = £40,000
£1,000,000 to £1,500,000 at 10% = £50,000
£1,500,000 to £2,000,000 at 12% = £60,000

Total = £165,000
```

Assignment
Write a calculator that returns the tax for both categories of buyers for a given property value,
you can use any programming language.

Example:

```
calculate(300000) would return something like {firstTimeBuyer: 2500, normalBuyer: 5000}
```

To test if your calculator works correctly, here are some sample answers below.

```
+------------------+--------------------+--------------+
| Property Amount  | First time buyer   | Normal       |
+------------------+--------------------+--------------+
| £100,000         | £0                 | £0           |
| £200,000         | £0                 | £1,500       |
| £300,000         | £2,500             | £5000        |
| £500,000         | £12,500            | £15,000      |
| £600,000         | £17,500            | £23,000      |
| £1,000,000       | £49,500            | £55,000      |
| £1,500,000       | £89,500            | £105,000     |
| £2,000,000       | £129,500           | £165,000     |
| £3,000,000       | £249,500           | £285,000     |
+------------------+--------------------+--------------+
```
