from rx.subject import Subject

subject_test = Subject()
subject_test.subscribe(
   lambda x: print("PRIMERO  {0}".format(x))
)
subject_test.subscribe(
   lambda x: print("SEGUNDO {0}".format(x))
)

subject_test.on_next("A")
subject_test.on_next("B")

