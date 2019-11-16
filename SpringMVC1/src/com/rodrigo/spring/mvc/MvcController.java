package com.rodrigo.spring.mvc;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class MvcController {

	@RequestMapping
	public String showPage() {
		
		return "examplePage1";
		
	}

}
