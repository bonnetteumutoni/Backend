def exam_results(*args, **kwargs):
    name = kwargs.get('name')
    course = kwargs.get('course')
    if len(args) == 0:
        print(f"Hello {name}, we don't have your results for {course}")
    elif len(args) == 1:
        print(f"Hello {name}, your average score for {course} is {args}")
    else:
        sumtotal = 0
        for score in args:
            sumtotal += score
        average = sumtotal / len(args)
        print(f"Hello {name}, your average score for {course} is {average}")
    
