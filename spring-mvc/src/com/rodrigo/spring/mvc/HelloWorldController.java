package com.rodrigo.spring.mvc;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/main")
public class HelloWorldController {
	
	
	@RequestMapping("/form")
	public String showsForm() {
		return "HelloWorld";
	}
	
	
	@RequestMapping("/output")
	public String processForm() {
		return "ProcessForm";
	}

	@RequestMapping("/outputTwo")
	public String anotherProcessForm(@RequestParam("name") String name, Model model) {
	//public String anotherProcessForm(HttpServletRequest request, Model model) {
		
		//String name = request.getParameter("name");
		
		String finalMessage = name + " is the choosen one.";
		
		// add dat to the Model
		
		model.addAttribute("message", finalMessage);
		
		return "ProcessForm";
		
	}
}
