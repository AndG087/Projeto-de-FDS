Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('test mediaempresa', () => {
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();
        
        cy.get('[href="/signupadmin/"]').click()
        cy.wait(1500)
        cy.get('#username').type("Lucas")
        cy.wait(1500)
        cy.get('#email').type("Lucas@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('a').click()
        cy.wait(1500)
        cy.get('#nome').type("Breno")
        cy.wait(1500)
        cy.get('#email').type("Breno@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('a').click()
        cy.wait(1500)
        cy.get('#nome').type("Arthur")
        cy.wait(1500)
        cy.get('#email').type("Arthur@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('#nome').type("Lucas")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get(':nth-child(6) > a').click()
        cy.wait(1500)
        cy.get('#avaliado').type("Arthur")
        cy.wait(1500)
        cy.get('[for="rating_4"]').click()
        cy.wait(1500)
        cy.get('.enviar-avaliacao').click()
        cy.wait(1500)
        cy.get(':nth-child(1) > a').click()
        cy.wait(1500)
        cy.get(':nth-child(8) > a').click()
        cy.wait(1500)
        cy.get(':nth-child(4) > a').click()
        cy.wait(1500)
        cy.get('#avaliado').type("Breno")
        cy.wait(1500)
        cy.get('[for="rating_3"]').click()
        cy.wait(1500)
        cy.get('.enviar-avaliacao').click()
        cy.wait(1500)
        cy.get(':nth-child(1) > a').click()
        cy.wait(1500)
    })
})