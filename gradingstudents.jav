class Result {


    public static List<Integer> gradingStudents(List<Integer> grades) {
        int n = grades.size();
         for (int i = 0; i< n; i++){
             if(grades.get(i) >= 38 && grades.get(i) % 5 >= 3){
                 grades.set(i, grades.get(i) + (5 - grades.get(i) % 5));
             }
             
         }
         return grades;

    }

}
