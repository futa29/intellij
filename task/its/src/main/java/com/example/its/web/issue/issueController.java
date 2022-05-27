package com.example.its.web.issue;

import java.util.List;
import java.util.Objects;

import com.example.its.domain.issue.issueEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class issueController {

    //Get /issue
    @GetMapping("/issues")
    public String showList(Model model){
            var issueList = List.of(
                    new issueEntity(1,"概要１","説明１"),
                    new issueEntity(2,"概要2","説明2"),
                    new issueEntity(3,"概要3","説明3")
            );
            model.addAttribute("issueList",issueList);
            return "issues/list";
    }
}
