package com.marek.loginnregistration.controller;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.marek.loginnregistration.models.LoginUser;
import com.marek.loginnregistration.models.User;
import com.marek.loginnregistration.services.UserService;

@Controller
public class HomeController {
	
	@Autowired
	private UserService userService;
	
    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("newUser", new User());
        model.addAttribute("newLogin", new LoginUser());
        return "index.jsp";
    }
    
    @PostMapping("/register")
    public String register(@Valid @ModelAttribute("newUser") User newUser, 
            BindingResult result, Model model, HttpSession session) {
        userService.register(newUser, result);
        if(result.hasErrors()) {
            model.addAttribute("newLogin", new LoginUser());
            return "index.jsp";
        }
        session.setAttribute("user_id", newUser.getId());
        return "redirect:/home";
    }
    
    @PostMapping("/login")
    public String login(@Valid @ModelAttribute("newLogin") LoginUser newLogin, 
            BindingResult result, Model model, HttpSession session) {
        User user = this.userService.login(newLogin, result);
        if(result.hasErrors()) {
            model.addAttribute("newUser", new User());
            return "index.jsp";
        }
        session.setAttribute("user_id", user.getId());
        return "redirect:/home";
    }
    
    @GetMapping("/home")
    public String logged(HttpSession session, Model model, RedirectAttributes redirectAttributes) {
    	Long loggedInUserId = (Long)session.getAttribute("user_id");
    	if(loggedInUserId == null) {
    		//generate flash message
    		redirectAttributes.addFlashAttribute("notAllowed", "You must log in first");
    		return "redirect:/";
    	}
    
    	
    	
    	//use the id from session to find a user in the db that has that id, to pass to the template
    	User loggedInUser = this.userService.findUser(loggedInUserId);
    	model.addAttribute("loggedInUser", loggedInUser);
    	
    	
    	return "home.jsp";
    }
    
    @GetMapping("/logout")
    public String logOut(HttpSession session) {
    	session.removeAttribute("user_id");
    	
    	return "redirect:/";
    }
    

}
