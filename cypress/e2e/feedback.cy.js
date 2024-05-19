describe('test feedbacks', () => {
    it('cenario1', () => {
        cy.visit('/');

        cy.get('#nome').type('Lucas')
        cy.get('[type="password"]').type('12345')
        cy.get('.submitbtn').click()
        cy.get('[type="Email"]').type('l@gmail.com')
        cy.get('textarea').type('Testando')
        cy.get('.btn-custom').click()
        cy.get(':nth-child(4) > a').click()
        cy.get('[data-bs-target="#exampleModal"]').click()
        
    })

})