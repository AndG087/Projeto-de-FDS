Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('test projetos pessoais', () => {
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();
        
        cy.get('[href="/signupadmin/"]').click()
        cy.wait(1500)
        cy.get('#username').type("User 1")
        cy.wait(1500)
        cy.get('#email').type("user@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('#nome').type('User 1')
        cy.wait(1500)
        cy.get('[type="password"]').type('12345')
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get(':nth-child(7) > a').click()
        cy.wait(1500)
        cy.get('#name').type('Projeto Legal')
        cy.wait(1500)
        cy.get('#description').type('Descrição Legal')
        cy.wait(1500)
        cy.get('#participants').type('User 1, User 2')
        cy.wait(1500)
        cy.get('#start_date').type("2024-06-20")
        cy.wait(1500)
        cy.get('#end_date').type("2024-06-27")
        cy.wait(1500)
        cy.get('.btn').click()
        cy.wait(1500)
        cy.get(':nth-child(4) > a').click()
        cy.wait(1500)
        cy.get('.card-body > .btn').click()
        cy.wait(1500)
    })

})

