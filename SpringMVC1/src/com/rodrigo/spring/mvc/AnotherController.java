package com.rodrigo.spring.mvc;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.stereotype.Controller;

@Controller
@RequestMapping("/secondary")
public class AnotherController {


	@RequestMapping("/form")
	public String showsForm() {
		return "HelloWorld";
	}
	
	@RequestMapping("/outputTwo")
	public String anotherProcessForm(@RequestParam("name") String name, Model model) {
	//public String anotherProcessForm(HttpServletRequest request, Model model) {
		
		//String name = request.getParameter("name");
		
		String finalMessage = name + " is not the choosen one.";
		
		// add dat to the Model
		
		model.addAttribute("message", finalMessage);
		
		return "ProcessForm";
		
	}
}
