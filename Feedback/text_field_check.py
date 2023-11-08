def neg(str):
    if str is None:
        return None
    negative_feeds = ['Unsatisfactory','Disappointing','Frustrating','Inadequate','Unacceptable','Dissatisfactory','Terrible','Horrible',
    'Awful','Poor','Bad','Worst','Negative','Upsetting','Disturbing','Annoying','Inferior','Faulty','Mistake','Displeasing']

    positive_feeds = ['Excellent',
'Outstanding',
'Exceptional',
'Fantastic',
'Wonderful',
'Great',
'Superb',
'Terrific',
'Amazing',
'Impressive',
'Pleasant',
'Satisfactory',
'Delightful',
'Brilliant',
'Fabulous',
'Awesome',
'Incredible',
'Perfect',
'Good',
'Marvelous',]

    for i in negative_feeds:
        i = i.lower()
        if i in str:
            return "negative"
        
    for i in positive_feeds:
        i = i.lower()
        if i in str:
            return "positive"