Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('test feedbacks', () => {
    
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get('a').click()
        cy.get('#nome').type("testfeedback")
        cy.get('#email').type("teste@gmail.com")
        cy.get('[type="password"]').type("12345")
        cy.get('.submitbtn').click()
        cy.get('#nome').type("testfeedback")
        cy.get('[type="password"]').type("12345")
        cy.get('.submitbtn').click()
        cy.get('[type="Email"]').type('teste@gmail.com')
        cy.get('textarea').type('site muito legal e divertido')
        cy.get('.btn-custom').click()
        cy.get(':nth-child(4) > a').click()
        cy.get('[data-bs-target="#exampleModal"]').click()

        
    })

})