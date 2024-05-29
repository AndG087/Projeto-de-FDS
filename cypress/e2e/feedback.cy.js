Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('test feedbacks', () => {
    
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get('[href="/signup/"]').click()
        cy.wait(1500)
        cy.get('#nome').type("testfeedback")
        cy.wait(1500)
        cy.get('#email').type("teste@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('#nome').type("testfeedback")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('[type="Email"]').type('teste@gmail.com')
        cy.wait(1500)
        cy.get('textarea').type('site muito legal e divertido')
        cy.wait(1500)
        cy.get('.btn-custom').click()
        cy.wait(1500)
        cy.get(':nth-child(4) > a').click()
        cy.wait(1500)
        cy.get('[data-bs-target="#exampleModal"]').click()
        cy.wait(1500)  
    })

})