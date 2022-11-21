import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Employee } from './employee';
import { EmployeeService } from './employee.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  
  public title = "Employee Manager App";
  
  public employees!: Employee[];
  
  public editEmployee!: Employee;
  
  public deleteEmployee!: Employee;


  constructor(private employeeService: EmployeeService) { }

  ngOnInit(): void {
    this.getEmployees();
  }

  public getEmployees(): void {
    this.employeeService.getEmployees().subscribe(
      (response: Employee[]) => {
        this.employees = response;
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      } 
    )
  }

  public searchEmployees(key: string): void {
    const results: Employee[] = [];

    for (const e of this.employees)
      if (e.name.toLowerCase().indexOf(key.toLowerCase()) !== -1 ||
        e.email.toLowerCase().indexOf(key.toLowerCase()) !== -1 ||
        e.name.toLowerCase().indexOf(key.toLowerCase()) !== -1 ||
        e.jobTitle.toLowerCase().indexOf(key.toLowerCase()) !== -1 ||
        e.phoneNumber.toLowerCase().indexOf(key.toLowerCase()) !== -1
      )
        results.push(e);
    
    this.employees = results;
    if (results.length === 0 || !key)
      this.getEmployees();
  }

  public onOpenModal(employee: Employee, mode: string): void {
    const container = document.getElementById('main-container');
    const button = document.createElement("button");
    button.type = "button";
    button.style.display = "none";
    button.setAttribute("data-toggle", "modal");

    if (mode === "add")
      button.setAttribute("data-target", "#addEmployeeModal");
    else if (mode === "edit") {
    console.log("button pressed");
      this.editEmployee = employee;
      button.setAttribute("data-target", "#updateEmployeeModal");
    }
    else if (mode === "delete") {
      this.deleteEmployee = employee;
      button.setAttribute("data-target", "#deleteEmployeeModal");
    }
    container?.appendChild(button);
    button.click();
  }

  public onAddEmployee(addForm: NgForm): void {
    // in order to close the modal after submit, click the close button
    document.getElementById("add-employee-form").click();
    // sent the values of form inside a json object 
    this.employeeService.addEmployee(addForm.value).subscribe(
      (response: Employee) => {
        console.log(response);
        // reload the employees
        this.getEmployees();
        addForm.reset();
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
        addForm.reset();
      }
    )
  }

  public onEditEmployee(employee: Employee): void {
    console.log(employee);
    
    this.employeeService.updateEmployee(employee).subscribe(
      (response: Employee) => {
        console.log(response);
        // reload the employees
        this.getEmployees();
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    )    
  }

  public onDeleteEmployee(employeeId: number): void {
    this.employeeService.deleteEmployee(employeeId).subscribe(
      (response: void) => {
        console.log(response);
        // reload the employees
        this.getEmployees();
      },
      (error: HttpErrorResponse) => {
        alert(error.message);
      }
    )
  }
}