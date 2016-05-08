import java.io.PrintWriter;
import java.util.Arrays;
import java.io.IOException;
public class ProblemGen {
	public static void main (String [] args) throws IOException{
		int min,max, arg1, arg2, soln;
		String question1,question2,category, sub_cat, topic_id;
		String[] problems = new String[400];
		PrintWriter math_problems = new PrintWriter("arithmetic.json","UTF-8");
		math_problems.println("{\"problems\": [");
		category = "math";
		sub_cat = "arithmetic";
		
		topic_id = "addition";
		for (int i=0; i < 100; i++) {
			min = 0;
			max = 100;
			
			do {
			arg1 = genArgs(min,max);
			arg2 = genArgs(min,max);
			question1 = Integer.toString(arg1)+" + " + Integer.toString(arg2) + " = ";
			question2 = Integer.toString(arg2)+" + " + Integer.toString(arg1) + " = ";
			}
			while (Arrays.asList(problems).contains(question1) || Arrays.asList(problems).contains(question2));
			
			soln = arg1 + arg2;
			problems[i] = question1;
			String answer = Integer.toString(soln);
			write(math_problems, question1, answer, i, category, sub_cat, topic_id);
		}
		
		topic_id = "subtraction";
		for (int i=100; i < 200; i++) {
			min = 0;
			max = 100;
			
			do {
			arg1 = genArgs(min,max);
			arg2 = genArgs(min,max);
			question1 = Integer.toString(arg1)+" - " + Integer.toString(arg2) + " = ";
			question2 = Integer.toString(arg2)+" - " + Integer.toString(arg1) + " = ";
			}
			while (Arrays.asList(problems).contains(question1) || Arrays.asList(problems).contains(question2));
			
			soln = arg1 - arg2;
			problems[i] = question1;
			String answer = Integer.toString(soln);
			write(math_problems, question1, answer, i, category, sub_cat, topic_id);
		}
		
		topic_id = "multiplication";
		for (int i=200; i < 300; i++) {
			min = 1;
			max = 20;
			
			do {
			arg1 = genArgs(min,max);
			arg2 = genArgs(min,max);
			question1 = Integer.toString(arg1)+" * " + Integer.toString(arg2) + " = ";
			question2 = Integer.toString(arg2)+" * " + Integer.toString(arg1) + " = ";
			}
			while (Arrays.asList(problems).contains(question1) || Arrays.asList(problems).contains(question2));
			
			soln = arg1 * arg2;
			problems[i] = question1;
			String answer = Integer.toString(soln);
			write(math_problems, question1, answer, i, category, sub_cat, topic_id);
		}
		
		topic_id = "division";
		for (int i=300; i < 400; i++) {
			min = 1;
			max = 100;
			
			do {
			arg1 = genArgs(min,max);
			arg2 = genArgs(min,max);
			question1 = Integer.toString(arg1)+" / " + Integer.toString(arg2) + " = ";
			question2 = Integer.toString(arg2)+" / " + Integer.toString(arg1) + " = ";
			}
			while (Arrays.asList(problems).contains(question1) || Arrays.asList(problems).contains(question2) || arg1 % arg2 != 0 || arg2 == 1 || arg1 == arg2);
			
			soln = arg1 / arg2;
			problems[i] = question1;
			String answer = Integer.toString(soln);
			if (i != 399) {
				write(math_problems, question1, answer, i, category, sub_cat, topic_id);
			}
			else {
				math_problems.println("{\"question\":\"" + question1 + 
						"\",\"id\":\"" + i + 
						"\",\"answer\":\"" + answer + 
						"\",\"category_id\":\"" + category +
						"\",\"sub_cat_id\":\"" + sub_cat +
						"\",\"topic_id\":\"" + topic_id +
						"\"}");
			}
		}
		math_problems.println("]}");
		math_problems.close();
	}
	
	public static int genArgs (int min, int max) {
		int i = min + (int)(Math.random() * ((max - min) + 1));
		return i;
	}
	
	public static void write (PrintWriter file,String question, String answer, int i, 
			String category, String sub_cat, String topic_id) {
		file.println("{\"question\":\"" + question + 
			"\",\"id\":\"" + i + 
			"\",\"answer\":\"" + answer + 
			"\",\"category_id\":\"" + category +
			"\",\"sub_cat_id\":\"" + sub_cat +
			"\",\"topic_id\":\"" + topic_id +
			"\"},");
	}
}
