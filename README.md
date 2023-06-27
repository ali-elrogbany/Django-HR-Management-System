# Django-HR-Management-System

Features:
  Manage Branches:
      View all branches in the system, including branch details.
      Create new branches and update existing ones.
      Delete branches from the system.
      Branches should have the following fields: name, building number, street, area, city, country, and an optional manager field.
      The manager field should only be visible on the branch update form and should be selected from a dropdown list of employees assigned to that branch.
      Viewing branch details should display a list of all employees assigned to that branch.
      Deleting a branch should also remove all employees assigned to it.
  Manage Employees:
      View all employees in the system, including employee details.
      Create new employees and update existing ones.
      Delete employees from the system.
      Employees should have the following fields: name, age, email, phone number, and branch.
      The branch field should be selected from a drop-down list of all branches.
      Deleting an employee who is the manager of a branch should not assign a new manager to that branch.
