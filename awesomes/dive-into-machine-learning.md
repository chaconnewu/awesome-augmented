<h1>
 Dive into Machine Learning
 <a href="http://creativecommons.org/licenses/by/4.0/">
  <img alt="Creative Commons License" src="http://i.creativecommons.org/l/by/4.0/88x31.png"/>
 </a>
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<p>
 <strong>
  Hi there! This guide is for you:
 </strong>
</p>
<ul>
 <li>
  <strong>
   You're new to
   <a href="https://en.wikipedia.org/wiki/Machine_learning">
    Machine Learning.
   </a>
  </strong>
 </li>
 <li>
  <strong>
   You know Python.
  </strong>
  (At least the basics! If you want to learn Python, try
  <a href="http://www.diveintopython.net/">
   Dive Into Python.
  </a>
  )
 </li>
</ul>
<p>
 I learned Python by hacking first, and getting serious
 <em>
  later.
 </em>
 I wanted to do this with Machine Learning. If this is your style, join me in getting a bit ahead of yourself.
</p>
<p>
 <em>
  Note:
 </em>
 There are several fields within "Data" and Machine Learning is just one. It's good to know the context:
 <a href="http://www.quora.com/What-is-the-difference-between-Data-Analytics-Data-Analysis-Data-Mining-Data-Science-Machine-Learning-and-Big-Data-1">
  What is the difference between Data Analytics, Data Analysis, Data Mining, Data Science, Machine Learning, and Big Data?
 </a>
</p>
<h1>
 Get your feet wet!
</h1>
<p>
 I suggest you get your feet wet ASAP. You'll boost your confidence.
</p>
<h2>
 Tools you'll need
</h2>
<ul>
 <li>
  <a href="https://www.python.org/">
   Python
  </a>
  . Python 3 is the best option.
 </li>
 <li>
  <a href="http://ipython.org/">
   IPython and the Jupyter Notebook
  </a>
  . (FKA IPython and IPython Notebook.)
 </li>
 <li>
  Some scientific computing packages:
  <ul>
   <li>
    numpy
   </li>
   <li>
    pandas
   </li>
   <li>
    scikit-learn
   </li>
   <li>
    matplotlib
   </li>
  </ul>
 </li>
</ul>
<p>
 You can install Python 3 and all of these packages in a few clicks with the
 <a href="https://www.continuum.io/downloads">
  Anaconda Python distribution
 </a>
 . Anaconda is popular in Data Science and Machine Learning communities.
</p>
<p>
 If you're using Python 2.7, don't worry. You don't have to migrate to Python 3 just for this guide. Also, if you're using pip/virtualenv instead of Anaconda, that's alright too! Cf.
 <a href="http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html">
  conda vs. pip vs. virtualenv
 </a>
 if you're curious.
</p>
<h2>
 Let's go!
</h2>
<p>
 <strong>
  <a href="http://opentechschool.github.io/python-data-intro/core/notebook.html">
   Learn how to use IPython Notebook
  </a>
  (5-10 minutes).
 </strong>
 (You can
 <a href="https://www.youtube.com/watch?v=qb7FT68tcA8">
  learn by screencast
 </a>
 instead.)
</p>
<p>
 Now, follow along with this brief exercise (10 minutes):
 <strong>
  <a href="http://scikit-learn.org/stable/tutorial/basic/tutorial.html">
   An introduction to machine learning with scikit-learn
  </a>
 </strong>
 . Do it in
 <code>
  ipython
 </code>
 or IPython Notebook. It'll really boost your confidence.
</p>
<p>
 <a href="http://scikit-learn.org/stable/tutorial/basic/tutorial.html">
  <img alt="I'll wait." src="http://i.imgur.com/nqn3pVV.jpg"/>
 </a>
</p>
<h2>
 What just happened?
</h2>
<p>
 You just classified some hand-written digits using [scikit-learn]. Neat huh?
</p>
<p>
 [scikit-learn] is the go-to library for machine learning in Python.
 <a href="http://scikit-learn.org/stable/testimonials/testimonials.html">
  Some recognizable logos use it, including Spotify and Evernote.
 </a>
 Machine learning is hard. You'll be glad your tools are easy to work with.
</p>
<p>
 I encourage you to look at the [scikit-learn] homepage  and spend about 5 minutes looking over the names of the strategies (Classification, Regression, etc.), and their applications. Don't click through yet! Just get a glimpse of the vocabulary.
</p>
<h1>
 Dive in
</h1>
<h2>
 A Visual Introduction to Machine Learning
</h2>
<p>
 Let's learn a bit more about Machine Learning, and a couple of common ideas and concerns. Read
 <a href="http://www.r2d3.us/visual-intro-to-machine-learning-part-1/">
  "A Visual Introduction to Machine Learning, Part 1"
 </a>
 by
 <a href="https://twitter.com/stephaniejyee">
  Stephanie Yee
 </a>
 and
 <a href="https://twitter.com/tonyhschu/">
  Tony Chu
 </a>
 .
</p>
<p>
 <a href="http://www.r2d3.us/visual-intro-to-machine-learning-part-1/">
  <img alt="A Visual Introduction to Machine Learning, Part 1" src="http://i.imgur.com/j5fiTBv.gif"/>
 </a>
</p>
<p>
 It won't take long. It's a beautiful introduction ... Try not to drool too much!
</p>
<h2>
 A Few Useful Things to Know about Machine Learning
</h2>
<p>
 OK. Let's dive deeper.
</p>
<p>
 Read
 <strong>
  <a href="http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf">
   "A Few Useful Things to Know about Machine Learning"
  </a>
 </strong>
 by Prof. Pedro Domingos. It's densely packed with valuable information, but not opaque. The author understands that there's a lot of "black art" and folk wisdom, and they invite you in.
</p>
<p>
 Take your time with this one. Take notes. Don't worry if you don't understand it all yet.
</p>
<p>
 The whole paper is packed with value, but I want to call out two points:
</p>
<ul>
 <li>
  <strong>
   Data alone is not enough.
  </strong>
  This is where science meets art in machine-learning. Quoting Domingos: "... the need for knowledge in learning should not be surprising. Machine learning is not magic; it can’t get something from nothing. What it does is get more from less. Programming, like all engineering, is a lot of work: we have to build everything from scratch. Learning is more like farming, which lets nature do most of the work. Farmers combine seeds with nutrients to grow crops. Learners combine knowledge with data to grow programs."
 </li>
 <li>
  <strong>
   More data beats a cleverer algorithm.
  </strong>
  Listen up, programmers. We like cool tools. Resist the temptation to reinvent the wheel, or to over-engineer solutions. Your starting point is to
  <a href="http://www.artima.com/intv/simplest3.html">
   Do the Simplest Thing that Could
   <em>
    Possibly
   </em>
   Work
  </a>
  . Quoting Domingos: "Suppose you’ve constructed the best set of features you can, but the classifiers you’re getting are still not accurate enough. What can you do now? There are two main choices: design a better learning algorithm, or gather more data. [...] As a rule of thumb, a dumb algorithm with lots and lots of data beats a clever one with modest amounts of it. (After all, machine learning is all about letting data do the heavy lifting.)"
 </li>
</ul>
<p>
 So
 <strong>
  knowledge
 </strong>
 and
 <strong>
  data
 </strong>
 are critical. Focus your efforts on those, before fussing about algorithms. In practice, this means that unless you
 <em>
  have
 </em>
 to increase complexity, you should continue to [Do Simple Things]; don't rush to neural networks just because they're cool. To improve your model, get more data  and use your knowledge of the problem to manipulate the data. You should spend most of your time on these steps. Only optimize your choice of algorithms after you've got enough data, and you've processed it well.
</p>
<p>
 <img alt="What has the most impact in Machine Learning" src="http://i1381.photobucket.com/albums/ah240/hangtwenty/Screen%20Shot%202015-03-05%20at%2010.08.10%20PM_zpsqnljkqt5.png"/>
</p>
<p>
 (Chart inspired by a slide from
 <a href="https://www.youtube.com/watch?v=TYVCVzEJhhQ">
  Alex Pinto's talk, "Secure Because Math: A Deep-Dive on ML-Based Monitoring"
 </a>
 .)
</p>
<h2>
 Talking Machines
</h2>
<p>
 Subscribe to
 <strong>
  <a href="http://www.thetalkingmachines.com/">
   Talking Machines
  </a>
 </strong>
 , a podcast about machine learning. It's great. It's a low-effort, high-yield way to learn more.
</p>
<p>
 I suggest this listening order:
</p>
<ul>
 <li>
  Start with the
  <a href="http://www.thetalkingmachines.com/blog/2015/4/23/starting-simple-and-machine-learning-in-meds">
   "Starting Simple"
  </a>
  episode. It supports what we read from Domingos. Ryan Adams talks about starting simple, as discussed above. Adams also stresses the importance of feature engineering. Feature engineering is an exercise of the "knowledge" Domingos writes about.
 </li>
 <li>
  Then, start over from the first episode
 </li>
</ul>
<h2>
 Play to learn
</h2>
<p>
 Pick
 <strong>
  one or two
 </strong>
 of these IPython Notebooks and play along.
</p>
<ul>
 <li>
  <a href="http://nbviewer.ipython.org/github/ogrisel/notebooks/blob/master/Labeled%20Faces%20in%20the%20Wild%20recognition.ipynb">
   Face Recognition on a subset of the Labeled Faces in the Wild
  </a>
 </li>
 <li>
  <a href="http://agconti.github.io/kaggle-titanic/">
   Machine Learning from Disaster
  </a>
  : Using Titanic data, "Demonstrates basic data munging, analysis, and visualization techniques. Shows examples of supervised machine learning techniques."
 </li>
 <li>
  <a href="https://github.com/jseabold/538model">
   Election Forecasting
  </a>
  : A replication of the model Nate Silver used to make
  <a href="http://fivethirtyeight.blogs.nytimes.com/fivethirtyeights-2012-forecast/">
   predictions about the 2012 US Presidential Election for the New York Times
  </a>
  )
  <sup>
   &#9733 169, pushed 276 days ago
  </sup>
 </li>
 <li>
  <a href="https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/example-data-science-notebook/Example%20Machine%20Learning%20Notebook.ipynb">
   An example Machine Learning notebook
  </a>
  : "let's pretend we're working for a startup that just got funded to create a smartphone app that automatically identifies species of flowers from pictures taken on the smartphone.  We've been tasked by our head of data science to create a demo machine learning model that takes four measurements from the flowers (sepal length, sepal width, petal length, and petal width) and identifies the species based on those measurements alone."
 </li>
 <li>
  ClickSecurity's "data hacking" series (thanks
  <a href="https://github.com/hummus">
   hummus
  </a>
  !)
  <ul>
   <li>
    <a href="http://nbviewer.ipython.org/github/ClickSecurity/data_hacking/blob/master/dga_detection/DGA_Domain_Detection.ipynb">
     Detect Algorithmically Generated Domains
    </a>
   </li>
   <li>
    <a href="http://nbviewer.ipython.org/github/ClickSecurity/data_hacking/blob/master/sql_injection/sql_injection.ipynb">
     Detect SQL Injection
    </a>
   </li>
   <li>
    <a href="http://nbviewer.ipython.org/github/ClickSecurity/data_hacking/blob/master/java_classification/java_classification.ipynb">
     Java Class File Analysis
    </a>
    : is this Java code malicious or benign?
   </li>
  </ul>
 </li>
 <li>
  If you want more of a data science bent, pick a notebook from
  <a href="https://github.com/donnemartin/data-science-ipython-notebooks">
   this excellent list of Data Science ipython notebooks
  </a>
  . "Continually updated Data Science Python Notebooks: Spark, Hadoop MapReduce, HDFS, AWS, Kaggle, scikit-learn, matplotlib, pandas, NumPy, SciPy, and various command lines."
  <sup>
   &#9733 5541, pushed 129 days ago
  </sup>
 </li>
 <li>
  Or more generic tutorials/overviews ...
  <ul>
   <li>
    <a href="http://amueller.github.io/sklearn_tutorial/">
     Tutorial introduction to machine learning with sklearn
    </a>
   </li>
   <li>
    <a href="http://bugra.github.io/work/notes/2014-11-22/an-introduction-to-supervised-learning-scikit-learn/">
     An Introduction to Supervised Learning via Scikit Learn
    </a>
   </li>
   <li>
    <a href="http://bugra.github.io/work/notes/2014-11-16/an-introduction-to-unsupervised-learning-scikit-learn/">
     An Introduction to Unsupervised Learning via Scikit Learn
    </a>
   </li>
  </ul>
 </li>
</ul>
<p>
 There are more places to find great IPython Notebooks:
</p>
<ul>
 <li>
  <a href="https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks#statistics-machine-learning-and-data-science">
   A Gallery of Interesting IPython notebooks (wiki page on GitHub): Statistics, Machine Learning and Data Science
  </a>
 </li>
 <li>
  <a href="http://nb.bianp.net/sort/views/">
   Fabian Pedregosa's larger, automatic gallery
  </a>
 </li>
</ul>
<h1>
 Immerse yourself
</h1>
<p>
 Pick one of the courses below and do the whole thing.
</p>
<h2>
 Recommended course
</h2>
<p>
 <strong>
  <a href="http://www.andrewng.org/about/">
   Prof. Andrew Ng's
  </a>
  <a href="https://www.coursera.org/learn/machine-learning">
   <em>
    Machine Learning
   </em>
  </a>
  is a free online course I've
  <a href="https://docs.google.com/document/d/1YN6BVdReNAYc8B0fjQ84yzDflqmeEPj7S0Xc-9_26R0/">
   seen
  </a>
  <a href="https://www.quora.com/How-do-I-learn-machine-learning-1/answer/Cory-Hicks-1">
   recommended
  </a>
  <a href="https://www.coursetalk.com/providers/coursera/courses/machine-learning?page=1&sort=-content_rating#reviews">
   often.
  </a>
  <a href="https://www.quora.com/How-do-I-learn-machine-learning-1/answer/Xavier-Amatriain">
   And
  </a>
  <a href="http://www.forbes.com/sites/anthonykosner/2013/12/29/why-is-machine-learning-cs-229-the-most-popular-course-at-stanford/">
   emphatically.
  </a>
 </strong>
</p>
<p>
 It's helpful if you decide on a pet project to play around with, as you go, so you have a way to apply your knowledge. You could use one of these
 <a href="https://github.com/caesar0301/awesome-public-datasets">
  Awesome Public Datasets
 </a>
 . And remember, IPython Notebook is your friend.
</p>
<p>
 Also, you should grab an in-depth textbook to use as a reference. The two best options are
 <a href="http://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/copy.html">
  <em>
   Understanding Machine Learning
  </em>
 </a>
 and
 <em>
  <a href="http://statweb.stanford.edu/~tibs/ElemStatLearn/">
   Elements of Statistical Learning
  </a>
 </em>
 . You'll see these recommended as reference textbooks.
 <a href="https://github.com/hangtwenty/dive-into-machine-learning/issues/29">
  I favor
  <em>
   UML
  </em>
  , but here's context and comparison.
 </a>
 Download both books, they're free.
</p>
<p>
 Busy schedule? Read
 <a href="http://rayli.net/blog/data/coursera-machine-learning-review/">
  Ray Li's review of this course
 </a>
 for some helpful tips.
</p>
<h2>
 Other courses
</h2>
<p>
 Here are some other free online courses I've seen recommended. (Machine Learning, Data Science, and related topics.)
</p>
<ul>
 <li>
  <a href="https://www.coursera.org/course/machlearning">
   Machine Learning
  </a>
  by Prof. Pedro Domingos of the University of Washington. Domingos wrote the paper
  <a href="https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf">
   "A Few Useful Things to Know About Machine Learning"
  </a>
  , from earlier in this guide. (Thanks to
  <a href="https://news.ycombinator.com/item?id=9563501">
   paperwork on Hacker News.
  </a>
  )
 </li>
 <li>
  Kevin Markham's video series,
  <a href="http://blog.kaggle.com/2015/04/08/new-video-series-introduction-to-machine-learning-with-scikit-learn/">
   Intro to Machine Learning with scikit-learn
  </a>
  , starts with what we've already covered, then continues on at a comfortable place. After the videos you could do Markham's
  <a href="https://github.com/justmarkham/DAT8">
   General Assembly's Data Science course.
  </a>
  Interactive. Markham's course is also offered in-person in Washington, DC.
 </li>
 <li>
  Data science courses as IPython Notebooks:
  <ul>
   <li>
    <a href="http://radimrehurek.com/data_science_python/">
     Practical Data Science
    </a>
   </li>
   <li>
    <a href="http://learnds.com/">
     Learn Data Science (an entire self-directed course!)
    </a>
   </li>
   <li>
    Supplementary material:
    <a href="https://github.com/donnemartin/data-science-ipython-notebooks">
     donnemartin/data-science-ipython-notebooks
    </a>
    . "Continually updated Data Science Python Notebooks: Spark, Hadoop MapReduce, HDFS, AWS, Kaggle, scikit-learn, matplotlib, pandas, NumPy, SciPy, and various command lines."
    <sup>
     &#9733 5541, pushed 129 days ago
    </sup>
   </li>
  </ul>
 </li>
 <li>
  Prof. Mark A. Girolami's
  <a href="https://github.com/josephmisiti/machine-learning-module">
   Machine Learning Module (GitHub Mirror).
  </a>
  Good for people with a strong mathematics background.
  <sup>
   &#9733 258, pushed 1957 days ago
  </sup>
 </li>
 <li>
  Surveys of Data Science courseware (a bit more Choose Your Own Adventure)
  <ul>
   <li>
    Check out
    <a href="https://www.quora.com/Is-it-worth-it-to-pay-9-*-49-for-a-data-science-specialization-on-Coursera/answer/Jack-Golding">
     Jack Golding's survey of Data Science courseware
    </a>
    . Includes Coursera's
    <a href="https://www.coursera.org/specializations/jhudatascience">
     Data Science Specialization
    </a>
    with 9 courses in it. The Specialization certificate isn't free, but you can take the courses 1-by-1 for free if you don't care about the certificate. The survey also covers
    <a href="http://cs109.github.io/2014/">
     Harvard CS109
    </a>
    which I've seen recommended elsewhere.
   </li>
   <li>
    <a href="https://www.quora.com/How-can-I-become-a-data-scientist?redirected_qid=59455">
     Another epic Quora thread: How can I become a data scientist?
    </a>
   </li>
   <li>
    Data Science Weekly's
    <a href="http://www.datascienceweekly.org/data-science-resources/the-big-list-of-data-science-resources">
     Big List of Data Science Resources
    </a>
    has a
    <a href="http://www.datascienceweekly.org/data-science-resources/data-science-moocs">
     List of Data Science MOOCs
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="http://cs109.github.io/2014/">
   Data Science (Harvard CS109)
  </a>
 </li>
 <li>
  <a href="http://stronginference.com/Bios8366/lectures.html">
   Advanced Statistical Computing (Vanderbilt BIOS8366).
  </a>
  . Interactive (lots of IPython Notebook material)
 </li>
</ul>
<h2>
 Learn Pandas well
</h2>
<p>
 If you're focusing on Python, you should get more familiar with Pandas.
</p>
<ul>
 <li>
  <strong>
   Essential
  </strong>
  :
  <a href="http://pandas.pydata.org/pandas-docs/stable/10min.html">
   10 Minutes to Pandas
  </a>
 </li>
 <li>
  <strong>
   Essential
  </strong>
  :
  <a href="http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/tutorials/things_in_pandas.ipynb">
   Things in Pandas I Wish I'd Had Known Earlier
  </a>
  (IPython Notebook)
 </li>
 <li>
  <a href="http://www.swegler.com/becky/blog/2014/08/06/useful-pandas-snippets/">
   Useful Pandas Snippets
  </a>
 </li>
 <li>
  Here are some docs I found especially helpful as I continued learning:
  <ul>
   <li>
    <a href="http://pandas.pydata.org/pandas-docs/stable/cookbook.html">
     Cookbook
    </a>
   </li>
   <li>
    <a href="http://pandas.pydata.org/pandas-docs/stable/dsintro.html">
     Data Structures
    </a>
    , esp.
    <a href="http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe">
     DataFrame
    </a>
    section
   </li>
   <li>
    <a href="http://pandas.pydata.org/pandas-docs/version/0.15.0/reshaping.html">
     Reshaping by pivoting DataFrames
    </a>
   </li>
   <li>
    <a href="http://pandas.pydata.org/pandas-docs/stable/computation.html">
     Computational tools
    </a>
    and
    <a href="http://stats.stackexchange.com/questions/29713/what-is-covariance-in-plain-language">
     StackExchange thread: "What is covariance in plain language?"
    </a>
   </li>
   <li>
    <a href="http://pandas.pydata.org/pandas-docs/stable/groupby.html">
     Group By (split, apply, and combine DataFrames)
    </a>
   </li>
   <li>
    <a href="http://pandas.pydata.org/pandas-docs/version/0.15.0/visualization.html">
     Visualizing your DataFrames
    </a>
   </li>
  </ul>
 </li>
</ul>
<h2>
 Cheat sheets
</h2>
<p>
 Bookmark these cheat sheets:
</p>
<ul>
 <li>
  <a href="http://scikit-learn.org/stable/tutorial/machine_learning_map/">
   scikit-learn algorithm cheat sheet
  </a>
 </li>
 <li>
  <a href="http://hunch.net/?p=2714">
   Metacademy: a package manager for [machine learning] knowledge
  </a>
  . A mind map of machine learning concepts, with great detail on each.
 </li>
 <li>
  <a href="https://drive.google.com/folderview?id=0ByIrJAE4KMTtaGhRcXkxNHhmY2M">
   Matplotlib / Pandas / Python cheat sheets
  </a>
  .
 </li>
</ul>
<h2>
 More topics
</h2>
<h3>
 More Data Science materials
</h3>
<p>
 Not repeating the materials mentioned above, here are some more Data Science resources:
</p>
<ul>
 <li>
  <strong>
   Extremely accessible data science book:
   <a href="http://www.john-foreman.com/data-smart-book.html">
    <em>
     Data Smart
    </em>
    by John Foreman
   </a>
  </strong>
 </li>
 <li>
  <strong>
   <a href="http://learnds.com/">
    An entire self-directed course in Data Science, as a IPython Notebook
   </a>
  </strong>
 </li>
 <li>
  <a href="http://cacm.acm.org/blogs/blog-cacm/169199-data-science-workflow-overview-and-challenges/fulltext">
   Data Science Workflow: Overview and Challenges
  </a>
  (read the article
  <em>
   and also
  </em>
  the comment by Joseph McCarthy)
 </li>
 <li>
  Fun little IPython Notebook:
  <a href="http://nbviewer.ipython.org/github/jmsteinw/Notebooks/blob/master/IndeedJobs.ipynb">
   Web Scraping Indeed.com for Key Data Science Job Skills
  </a>
 </li>
 <li>
  Swami Chandrasekaran's
  <a href="http://nirvacana.com/thoughts/becoming-a-data-scientist/">
   "Becoming a Data Scientist"
  </a>
  is a concise, printable picture of a data science curriculum
 </li>
</ul>
<h3>
 Bayesian Statistics and Machine Learning
</h3>
<p>
 From
 <a href="https://metacademy.org/roadmaps/rgrosse/bayesian_machine_learning">
  the "Bayesian Machine Learning" overview on Metacademy
 </a>
 :
</p>
<blockquote>
 <p>
  ... Bayesian ideas have had a big impact in machine learning in the past 20 years or so because of the flexibility they provide in building structured models of real world phenomena. Algorithmic advances and increasing computational resources have made it possible to fit rich, highly structured models which were previously considered intractable.
 </p>
</blockquote>
<p>
 You can learn more by studying one of the following resources. Both resources use Python,
 <a href="https://github.com/pymc-devs/pymc">
  PyMC
 </a>
 , and Jupyter Notebooks.
* The
 <strong>
  free book,
 </strong>
 <em>
  <a href="http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/">
   Probabilistic Programming and Bayesian Methods for Hackers
  </a>
  .
 </em>
 Made with a "computation/understanding-first, mathematics-second point of view." It's available in print too!
*
 <a href="https://github.com/markdregan/Bayesian-Modelling-in-Python">
  Bayesian Modelling in Python
 </a>
</p>
<h2>
 Questions, answers, chats
</h2>
<p>
 For now, the best StackExchange site is
 <a href="http://stats.stackexchange.com/questions/tagged/machine-learning?sort=frequent&pageSize=15">
  stats.stackexchange.com –
  <em>
   machine-learning
  </em>
  .
 </a>
 (There's also
 <a href="http://datascience.stackexchange.com/">
  datascience.stackexchange.com
 </a>
 , but it's still in Beta.) And there's
 <a href="https://www.reddit.com/r/machinelearning">
  /r/machinelearning
 </a>
 . There are also many relevant discussions on Quora, for example:
 <a href="http://www.quora.com/What-is-the-difference-between-Data-Analytics-Data-Analysis-Data-Mining-Data-Science-Machine-Learning-and-Big-Data-1">
  What is the difference between Data Analytics, Data Analysis, Data Mining, Data Science, Machine Learning, and Big Data?
 </a>
</p>
<p>
 You should also
 <a href="https://gitter.im/scikit-learn/scikit-learn">
  join the Gitter channel for scikit-learn!
 </a>
</p>
<p>
 For help and community in meatspace, seek out meetups. Data Science Weekly's
 <a href="http://www.datascienceweekly.org/data-science-resources/the-big-list-of-data-science-resources">
  Big List of Data Science Resources
 </a>
 may help you.
</p>
<h1>
 Assorted Opinions and Other Resources
</h1>
<p>
 The rest of the stuff that might not be structured enough for a course, but seems important to know.
</p>
<h2>
 Risks
</h2>
<p>
 "Machine learning systems automatically learn programs from
data." Pedro Domingos, in
 <a href="http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf">
  "A Few Useful Things to Know about Machine Learning."
 </a>
 The programs you generate will require maintenance. Like any way of creating programs faster, you can rack up technical debt.
</p>
<p>
 Here is the abstract of
 <a href="https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/43146.pdf">
  Machine Learning: The High-Interest Credit Card of Technical Debt
 </a>
 :
</p>
<blockquote>
 <p>
  Machine learning offers a fantastically powerful toolkit for building complex systems quickly. This paper argues that it is dangerous to think of these quick wins as coming for free. Using the framework of technical debt, we note that it is remarkably easy to incur massive ongoing maintenance costs at the system level when applying machine learning. The goal of this paper is highlight several machine learning specific risk factors and design patterns to be avoided or refactored where possible. These include boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, changes in the external world, and a variety of system-level anti-patterns.
 </p>
</blockquote>
<p>
 If you're following this guide, you should read that paper. You can also
 <a href="http://softwareengineeringdaily.com/2015/11/17/machine-learning-and-technical-debt-with-d-sculley/">
  listen to a podcast episode interviewing one of the authors of this paper
 </a>
 .
</p>
<p>
 A few more articles on the risks:
</p>
<ul>
 <li>
  <strong>
   <a href="http://www.john-foreman.com/blog/surviving-data-science-at-the-speed-of-hype">
    Surviving Data Science "at the Speed of Hype"
   </a>
  </strong>
  by John Foreman, Data Scientist at MailChimp
 </li>
 <li>
  <a href="http://www.kdnuggets.com/2015/01/high-cost-machine-learning-technical-debt.html">
   The High Cost of Maintaining Machine Learning Systems
  </a>
 </li>
 <li>
  <a href="http://hunch.net/?p=22">
   11 Clever Methods of Overfitting and How to Avoid Them
  </a>
 </li>
 <li>
  <a href="http://www.john-foreman.com/blog/the-perilous-world-of-machine-learning-for-fun-and-profit-pipeline-jungles-and-hidden-feedback-loops">
   The Perilous World of Machine Learning for Fun and Profit: Pipeline Jungles and Hidden Feedback Loops
  </a>
 </li>
</ul>
<h3>
 Welcome to the Danger Zone
</h3>
<p>
 So you are dabbling with Machine Learning. You've got Hacking Skills. Maybe you've got some "knowledge" in Domingos' sense (some "Substantive Expertise" or "Domain Knowledge"). This diagram is modified slightly from Drew Conway's "Data Science Venn Diagram." It isn't a
 <em>
  perfect
 </em>
 fit for us, but it may get the point across:
</p>
<p>
 <a href="http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram">
  <img alt="Drew Conway's Data Science Venn Diagram, modified slightly" src="http://i.imgur.com/cH5Rkko.png"/>
 </a>
</p>
<p>
 <strong>
  Please
 </strong>
 don't sell yourself as a Machine Learning expert while you're still in the Danger Zone. Don't build bad products or publish junk science. (Also please
 <a href="http://arstechnica.co.uk/security/2016/02/the-nsas-skynet-program-may-be-killing-thousands-of-innocent-people/">
  don't be evil
 </a>
 .) This guide can't tell you how you'll know you've "made it" into Machine Learning competence ... let alone expertise. It's hard to evaluate proficiency without schools or other institutions. This is a common problem for self-taught people.
</p>
<h4>
 Towards Expertise
</h4>
<p>
 You need practice.
 <a href="https://news.ycombinator.com/item?id=10508565">
  On Hacker News, user olympus commented to say you could use competitions to practice and evaluate yourself
 </a>
 .
 <a href="http://www.kaggle.com/competitions">
  Kaggle
 </a>
 and
 <a href="http://www.chalearn.org/">
  ChaLearn
 </a>
 are hubs for Machine Learning competitions. You can find some
 <a href="https://github.com/apeeyush/machine-learning">
  examples of code for popular Kaggle competitions here
 </a>
 . For smaller exercises,
 <a href="https://www.hackerrank.com/domains/ai/machine-learning/page/1">
  try HackerRank
 </a>
 .
</p>
<p>
 You also need understanding. You should review what Kaggle competition winners say about their solutions,
 <a href="http://blog.kaggle.com/">
  for example, the "No Free Hunch" blog
 </a>
 . These might be over your head at first but once you're starting to understand and appreciate these, you know you're getting somewhere.
</p>
<p>
 Competitions and challenges are one way to practice. You shouldn't limit yourself, though - and you should also understand that
 <a href="http://jvns.ca/blog/2014/06/19/machine-learning-isnt-kaggle-competitions">
  Machine Learning isn't
  <strong>
   all
  </strong>
  about Kaggle competitions
 </a>
 .
</p>
<p>
 Here's a complementary way to practice:
 <strong>
  do practice studies.
 </strong>
</p>
<ol>
 <li>
  <strong>
   Ask a question. Start your own study.
  </strong>
  The
  <a href="https://github.com/DataScienceSpecialization/courses/blob/master/01_DataScientistToolbox/03_02_whatIsData/index.Rmd#the-data-is-the-second-most-important-thing">
   "most important thing in data science is the question"
  </a>
  (
  <a href="https://github.com/jtleek">
   Dr. Jeff T. Leek
  </a>
  ). So start with a question. Then, find
  <a href="https://github.com/caesar0301/awesome-public-datasets">
   real data
  </a>
  . Analyze it. Then ...
 </li>
 <li>
  <strong>
   Communicate results.
  </strong>
  When you have a novel finding, reach out for peer review.
 </li>
 <li>
  <strong>
   Fix issues.
  </strong>
  Learn. Share what you learn.
 </li>
</ol>
<p>
 And repeat. Re-phrasing this, it fits with the
 <a href="https://en.wikipedia.org/wiki/Scientific_method">
  scientific method
 </a>
 : formulate a question (or problem statement), create a hypothesis, gather data, analyze the data, and communicate results. (You should
 <a href="http://101.datascience.community/2012/06/27/the-data-scientific-method/">
  watch this video about the scientific method in data science
 </a>
 , and/or
 <a href="http://customerthink.com/getting-insights-using-data-science-skills-and-the-scientific-method/">
  read this article
 </a>
 .)
</p>
<p>
 How can you come up with interesting questions? Here's one way. Every Sunday,
 <a href="https://github.com/caesar0301/awesome-public-datasets">
  browse datasets
 </a>
 and write down some questions. Also, sign up for
 <a href="https://tinyletter.com/data-is-plural">
  Data is Plural
 </a>
 , a newsletter of interesting datasets; look at these, datasets, and write down questions. Stay curious. When a question inspires you, start a study.
</p>
<p>
 This advice, to do practice studies and learn from peer review, is based on
 <a href="https://github.com/hangtwenty/dive-into-machine-learning/issues/11#issuecomment-153934120">
  a conversation
 </a>
 with
 <a href="http://www.randalolson.com/">
  Dr. Randal S. Olson
 </a>
 . Here's more advice from Olson,
 <a href="https://github.com/hangtwenty/dive-into-machine-learning/issues/11#issuecomment-154135498">
  quoted with permission:
 </a>
</p>
<blockquote>
 <p>
  I think the best advice is to tell people to always present their methods clearly and to avoid over-interpreting their results. Part of being an expert is knowing that there's rarely a clear answer, especially when you're working with real data.
 </p>
</blockquote>
<p>
 As you repeat this process, your practice studies will become more scientific, interesting, and focused. The most important part of this process is peer review.
</p>
<h4>
 Ask for Peer Review
</h4>
<p>
 Here are some communities where you can reach out for peer review:
</p>
<ul>
 <li>
  <a href="https://stats.stackexchange.com/">
   Cross-Validated: stats.stackexchange.com
  </a>
 </li>
 <li>
  <a href="https://reddit.com/r/DataIsBeautiful">
   /r/DataIsBeautiful
  </a>
 </li>
 <li>
  <a href="https://reddit.com/r/DataScience">
   /r/DataScience
  </a>
 </li>
 <li>
  <a href="https://reddit.com/r/MachineLearning">
   /r/MachineLearning
  </a>
 </li>
 <li>
  <a href="https://news.ycombinator.com">
   Hacker News: news.ycombinator.com
  </a>
  . You'll probably want to submit as "Show HN"
 </li>
</ul>
<p>
 Post to any of those, and ask for feedback. You'll get feedback. You'll learn a ton. As experts review your work you will learn a lot about the field. You'll also be practicing a crucial skill: accepting critical feedback.
</p>
<p>
 When I read the feedback on my Pull Requests, first I repeat to myself, "I will not get defensive, I will not get defensive, I will not get defensive." You may want to do that before you read reviews of your Machine Learning work too.
</p>
<h3>
 An Anecdote About User Experience
</h3>
<p>
 If you create software for users, and you want to use machine learning to benefit your users,
 <em>
  you must understand your users.
 </em>
 I won't get into a whole user experience rant here, but in short, you must think about user experience.
</p>
<p>
 I have a friend who worked at
 <code>
  <Redacted>
 </code>
 Music Streaming Service. This company used machine learning in their recommendation and radio services. He complained about the way the company scored the radio feature's performance. There was disagreement about what should be scored. They used a metric, "no song skips." But why? Sure that indicates the recommendation wasn't
 <em>
  awful
 </em>
 , what if you want to measure engagement? Other metrics could measure positive engagement: "favorites," shares, listening time, or whether the listener returns to the radio station later. Measuring "no skips" might work for the passive listener, but the engaged listener is different. Perhaps the engaged listener will skip 5 songs, but find 20 songs they love and come back to the service later.
</p>
<p>
 <strong>
  My takeaway:
 </strong>
 user experience matters just as much as ever. You must understand
 <em>
  which kind
 </em>
 of user you're trying to benefit with your machine learning techniques. Write user stories. (Some readers may notice this anecdote is very unscientific. Well, user stories are sometimes unscientific. Yet still so important.)
</p>
<p>
 Try to measure success
 <em>
  for your users.
 </em>
 You must be able to measure before you can optimize.
</p>
<p>
 It helps to have knowledge of the domain (substantive expertise). You may also benefit from UX expertise. Work with UX experts if you can.
</p>
<h3>
 Machine Learning in Internet Security
</h3>
<p>
 There was a great BlackHat webcast on this topic,
 <a href="https://www.blackhat.com/html/webcast/02192015-secure-because-math.html">
  Secure Because Math: Understanding Machine Learning-Based Security Products.
 </a>
 Slides are
 <a href="https://www.blackhat.com/html/webcast/02192015-secure-because-math.html">
  here
 </a>
 ,
 <a href="https://attendee.gotowebinar.com/recording/80449431422110210">
  video recording is here.
 </a>
 Equally relevant to InfoSec and AppSec.
</p>
<h3>
 Deep Learning
</h3>
<p>
 In early editions of this guide, there was no specific "Deep Learning" section. I omitted it intentionally. I think it is not effective for us to jump too far ahead. I also know that if you become an expert in traditional Machine Learning, you'll be capable of moving onto advanced subjects like Deep Learning, whether or not I've put that in this guide. We're just trying to get you started here!
</p>
<p>
 Maybe this is a way to check your progress: ask yourself, does Deep Learning seem like magic? If so, take that as a sign that you aren't ready to work with it professionally. Let the fascination motivate you to learn more. I have read some argue you can learn Deep Learning in isolation; I have read others recommend it's best to master traditional Machine Learning first. Why not start with traditional Machine Learning, and develop your reasoning and intuition there? You'll only have an easier time learning Deep Learning after that. After all of it, you'll able to tackle all sorts of interesting problems.
</p>
<p>
 In any case, when you decide you're ready to dive into Deep Learning, here are some helpful resources.
</p>
<ul>
 <li>
  <strong>
   <a href="http://www.deeplearningbook.org/">
    <em>
     Deep Learning
    </em>
   </a>
   , a free book published MIT Press.
  </strong>
  By Ian Goodfellow, Yoshua Bengio and Aaron Courville
 </li>
 <li>
  <a href="https://www.quora.com/What-are-the-best-ways-to-pick-up-Deep-Learning-skills-as-an-engineer">
   Quora: "What are the best ways to pick up Deep Learning skills as an engineer?"
  </a>
  — answered by Greg Brockman (Co-Founder & CTO at OpenAI, previously CTO at Stripe)
 </li>
</ul>
<h3>
 "Big" Data?
</h3>
<p>
 Scaling data analysis is a familiar problem now, and there's no shortage of ways to address it.
 <a href="http://www.john-foreman.com/blog/surviving-data-science-at-the-speed-of-hype">
  Beware needless hype and companies selling you flashy, proprietary solutions.
 </a>
 You can do it all with open-source tools. Even if "buy" instead of "build," you may want to buy from vendors who use known good stacks. No news here.
</p>
<p>
 Here are some open-source tools to reach for:
</p>
<ul>
 <li>
  <strong>
   <a href="https://spark.apache.org/">
    Apache Spark.
   </a>
  </strong>
  <ul>
   <li>
    I mean, hell,
    <a href="https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html">
     Spark has DataFrames and easy co-operability with pandas!
    </a>
   </li>
   <li>
    Berkeley has
    <a href="https://www.edx.org/course/scalable-machine-learning-uc-berkeleyx-cs190-1x#.VOC70VPF_lQ">
     a course on Scalable Machine Learning, focusing on Apache Spark.
    </a>
   </li>
  </ul>
 </li>
 <li>
  <a href="http://netflix.github.io/#repo">
   NetflixOSS
  </a>
  (see "Big Data Tools")
  <ul>
   <li>
    <a href="http://techblog.netflix.com/2015/01/introducing-surus-and-scorepmml.html">
     Netflix: Surus and ScorePMML
    </a>
   </li>
   <li>
    <a href="http://techblog.netflix.com/search/label/big%20data">
     "big data" on the NetflixOSS blog
    </a>
   </li>
  </ul>
 </li>
</ul>
<p>
 And here are some things to read and listen to:
</p>
<ul>
 <li>
  <a href="http://simplystatistics.org/2014/05/22/10-things-statistics-taught-us-about-big-data-analysis/">
   10 things statistics taught us about big data analysis
  </a>
  (and some more food for thought:
  <a href="http://www.datasciencecentral.com/profiles/blogs/what-statisticians-think-about-data-scientists">
   "What Statisticians think about Data Scientists"
  </a>
  )
 </li>
 <li>
  <a href="http://www.thetalkingmachines.com/blog/2015/6/4/the-economic-impact-of-machine-learning-and-using-the-kernel-trick-to-dig-in-to-big-data">
   "Talking Machines" #12
  </a>
  : Interviews Prof. Andrew Ng (from
  <a href="https://www.coursera.org/learn/machine-learning">
   our main course, which has its own module on big data
  </a>
  ); this episode covers some problems relevant to
  <em>
   high-dimensional
  </em>
  data
 </li>
 <li>
  <a href="http://www.thetalkingmachines.com/blog/2015/7/16/really-really-big-data-and-machine-learning-in-business">
   "Talking Machines" #15: "Really Really Big Data and Machine Learning in Business"
  </a>
 </li>
 <li>
  Free eBook,
  <a href="http://www.tamr.com/landing-pages/getting-data-right/">
   <em>
    Getting Data Right: Tackling the Challenges of
Big Data Volume and Variety
   </em>
  </a>
  by Michael Stonebraker, Tom Davenport, James Markarian, and others, published by O'Reilly. You can
  <a href="https://soundcloud.com/oreilly-radar/the-future-of-data-at-scale">
   listen to an accompanying podcast
  </a>
  too.
 </li>
</ul>
<h2>
 Finding Open-Source Libraries
</h2>
<ul>
 <li>
  Bookmark
  <strong>
   <a href="https://github.com/josephmisiti/awesome-machine-learning">
    awesome-machine-learning
   </a>
  </strong>
  , a curated list of
  <a href="https://github.com/bayandin/awesome-awesomeness">
   awesome
  </a>
  Machine Learning libraries and software.
  <sup>
   &#9733 12665, pushed 129 days ago
  </sup>
 </li>
 <li>
  Bookmark
  <a href="https://github.com/svaksha/pythonidae/blob/master/AI.md#machine-learning">
   Pythonidae
  </a>
  , a curated list of
  <a href="https://github.com/bayandin/awesome-awesomeness">
   awesome
  </a>
  libraries and software in the Python language - with a section on Machine Learning.
 </li>
 <li>
  Bookmark
  <a href="https://github.com/svaksha/Julia.jl/blob/master/AI.md#machine-learning">
   Julia.jl
  </a>
  , a curated list of
  <a href="https://github.com/bayandin/awesome-awesomeness">
   awesome
  </a>
  libraries and software in the Julia language - with a section on Machine Learning.
 </li>
 <li>
  <a href="http://www.tensorflow.org/">
   TensorFlow
  </a>
  seems like a
  <a href="https://news.ycombinator.com/item?id=10532957">
   really big deal.
  </a>
  People like you will do exciting things with TensorFlow. It's a framework. Frameworks can help you manage complexity. Just remember this rule of thumb:
  <strong>
   "More data beats a cleverer algorithm"
  </strong>
  (Domingos), no matter how cool your tools are. Also note, TensorFlow is not the only machine learning framework of its kind:
  <strong>
   <a href="https://github.com/zer0n/deepframeworks">
    Check this great, detailed comparison of TensorFlow, Torch, and Theano.
   </a>
  </strong>
  See also
  <a href="https://github.com/Newmu/Theano-Tutorials">
   Newmu/Theano-Tutorials
  </a>
  and
  <a href="https://github.com/nlintz/TensorFlow-Tutorials">
   nlintz/TensorFlow-Tutorials
  </a>
  . See also the section on Deep Learning above.
 </li>
 <li>
  For Machine-Learning libraries that might not be on PyPI, GitHub, etc., there's
  <a href="http://mloss.org/software/">
   MLOSS (Machine Learning Open Source Software)
  </a>
  . Seems to feature many academic libraries.
 </li>
 <li>
  <a href="http://www.creativeai.net/">
   CreativeAi.net
  </a>
  . OK not exactly about
  <em>
   libraries
  </em>
  , but this is often intriguing, and worth subscribing to  ... warning, it's easy to get sucked in :)
 </li>
</ul>
<h2>
 Alternative ways to "Dive into Machine Learning"
</h2>
<p>
 Here are some other guides to Machine Learning. They can be alternatives or complements to this guide.
</p>
<ul>
 <li>
  <a href="http://sebastianraschka.com/faq/docs/ml-curriculum.html">
   "How would your curriculum for a machine learning beginner look like?"
  </a>
  by Sebastian Raschka. A selection of the core online courses and books for getting started with machine learning and gaining expert knowledge. It contextualizes Raschka's own book,
  <a href="https://github.com/rasbt/python-machine-learning-book">
   <em>
    Python Machine Learning
   </em>
  </a>
  (which I would have linked to anyway!) See also
  <a href="https://github.com/rasbt/pattern_classification">
   <code>
    pattern_classification
   </code>
   GitHub repository
  </a>
  maintained by the author, which contains IPython notebooks about various machine learning algorithms and various data science related resources.
 </li>
 <li>
  <a href="http://www.jacksimpson.co/2015/06/07/materials-for-learning-machine-learning/">
   Materials for Learning Machine Learning
  </a>
  by Jack Simpson
 </li>
 <li>
  <a href="http://xyclade.github.io/MachineLearning/">
   Machine Learning for Developers
  </a>
  is another good introduction, perhaps better if you're more familiar with Java or Scala. It introduces machine learning for a developer audience using Smile, a machine learning library that can be used both in Java and Scala.
 </li>
 <li>
  <a href="https://gist.github.com/hangtwenty/a15c8bed5b120eebf352">
   Machine Learning for Programmers [with caveats]
  </a>
  : Pragmatic guide for developers, definitely worth a read. I've linked you to my own intro to it, explaining a few caveats. Taking it with a grain of salt, and these caveats in mind, I think some programmers will find it worth their time.
 </li>
 <li>
  <a href="https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/example-data-science-notebook/Example%20Machine%20Learning%20Notebook.ipynb">
   Example Machine Learning notebook, exercise, and guide
  </a>
  by Dr. Randal S. Olson. Mentioned in Notebooks section as well, but it has a similar goal to this guide (introduce you, and show you where to go next). Rich "Further Reading" section.
 </li>
 <li>
  [Your guide here]
 </li>
</ul>
