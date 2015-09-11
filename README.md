# Intro to Hadoop and MapReduce (Udacity)

This repository contains all of my code for the final project.

##Students and Posting Time on Forums
Problem description:
>We have a lot of passionate students that bring a lot of value to forums. Forums also sometimes need a watchful eye on them, to make sure that posts are tagged in a way that helps to find them, that the tone on forums stays positive, and in general - they need people who can perform some management tasks - forum moderators. These are usually chosen from students who already have shown that they are active and helpful forum participants.

>Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.

>In this exercise your task is to find for each student what is the hour during which the student has posted the most posts. Output from reducers should be:

>`author_id    hour`

>For example:

>`13431511\t13`

>`54525254141\t21`

>If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines. The order in which these lines appear in your output does not matter.

>You can ignore the time-zone offset for all times - for example in the following line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

>In order to find the hour posted, please use the date_added field and NOT the last_activity_at field.

My solutions:
* [`student_times_mapper.py`](student_times_mapper.py)
* [`student_times_reducer.py`](student_times_reducer.py)

##Post and Answer Length
Problem description:
>We are interested to see if there is a correlation between the length of a post and the length of answers.

>Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get the required result.

My solutions:
* [`average_length_mapper.py`](average_length_mapper.py)
* [`average_length_reducer.py`](average_length_reducer.py)

##Top Tags
Problem description:
>We are interested seeing what are the top tags used in posts.

>Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

>For an extra challenge you can think about how to get a top 10 list of tags, where they are ordered by some weighted score of your choice. If you decide to do this, then please submit your solution to the regular problem and then also submit this extra challenge problem in separate files as described on the instruction page.

My solutions:
* [`popular_tags_mapper.py`](popular_tags_mapper.py)
* [`popular_tags_reducer.py`](popular_tags_reducer.py)
I also created a version where tags are sorted based on their total score:
* [`popular_tags_extra_mapper.py`](popular_tags_extra_mapper.py)
* [`popular_tags_extra_reducer.py`](popular_tags_extra_reducer.py)
