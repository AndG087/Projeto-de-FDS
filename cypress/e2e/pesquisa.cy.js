Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('test pesquisa', () => {
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get('[href="/signupadmin/"]').click()
        cy.wait(1500)
        cy.get('#username').type("Lucas")
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
        cy.get(':nth-child(7) > a').click()
        cy.wait(1500)
        cy.get('#name').type("Projeto Legal")
        cy.wait(1500)
        cy.get('#description').type("Descrição Qualquer")
        cy.wait(1500)
        cy.get('#participants').type("João")
        cy.wait(1500)
        cy.get('#start_date').type("2024-06-12")
        cy.wait(1500)
        cy.get('#end_date').type("2024-06-19")
        cy.wait(1500)
        cy.get('.btn').click()
        cy.wait(1500)
        cy.get(':nth-child(9) > a').click()
        cy.wait(1500)
        cy.get('input').type("Projeto Legal")
        cy.wait(1500)
        cy.get('button').click()
        cy.wait(1500)
    })
    it('cenario2', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get('[href="/signup/"]').click()
        cy.wait(1500)
        cy.get('#nome').type("Arthur")
        cy.wait(1500)
        cy.get('#email').type("A@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('a').click()
        cy.wait(1500)
        cy.get('#nome').type("Breno")
        cy.wait(1500)
        cy.get('#email').type("B@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('#nome').type('Breno')
        cy.wait(1500)
        cy.get('[type="password"]').type('12345')
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get(':nth-child(8) > a').click()
        cy.wait(1500)
        cy.get('input').type("Arthur")
        cy.wait(1500)
        cy.get('button').click()
        cy.wait(1500)
    })
    it('cenario3', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get('[href="/signup/"]').click()
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
        cy.get(':nth-child(8) > a').click()
        cy.wait(1500)
        cy.get('input').type("Cesar")
        cy.wait(1500)
        cy.get('button').click()
        cy.wait(1500)
    })

})