Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('test perfil', () => {
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get('a').click()
        cy.wait(1500)
        cy.get('#nome').type("Lucas")
        cy.wait(1500)
        cy.get('#email').type("l@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('#nome').type('Lucas')
        cy.wait(1500)
        cy.get('[type="password"]').type('12345')
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get(':nth-child(4) > a').click()
        cy.wait(1500)
        cy.get('a > .btn').click()
        cy.wait(1500)
        cy.get('#foto').type("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLsVGov5C1gQgknbN7IKQJ5r_Qaw1RBDifLw&usqp=CAU")
        cy.wait(1500)
        cy.get('#informacoes_usuario').type("Funcionário da empresa x")
        cy.wait(1500)
        cy.get('.btn-primary').click()
        cy.wait(1500)
    })

})