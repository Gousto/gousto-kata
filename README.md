# Gousto Kata

At Gousto we send boxes of ingredients to customers to cook at home and create their perfect dinner. Customers are able to choose multiple recipes for a different number of people. This means the number of ingredients in a box can vary, and the volume of those ingredients can vary by even more.

![Intelligent Packaging Explained](https://i.imgur.com/8iPoykn.png)

## The Problem

In this test you'll be given two JSON files.

- `boxes.json`

  - This contains an array of different box sizes available for us to send an order in. Each box will have an ID and dimensions.

- `orders.json`.
  - This contains an array of orders, each order contains an ID and an array of ingredients. These ingredients will have a volume.

We'd like you to build an app (command line, REST service, whatever you desire) which takes these two files processes them and determines the smallest possible box that the order will fit into. We call this feature **Intelligent Packaging**

## Expected Output

Once you have the smallest possible box that fits all the ingredients we'd like you to return a list of the order IDs and the IDs of the boxes you've matched against them.

## The Rules

Approach this problem any way you like, you can build a RESTful service, a command line app or a simple script.

Use whatever language, technology or framework you're most comfortable with to approach the problem.

Feel free to ask questions and think out loud, we're more interested in seeing how you think and approach the problem than we are a working solution.

We don't expect for you to complete the exercise in the given time.
