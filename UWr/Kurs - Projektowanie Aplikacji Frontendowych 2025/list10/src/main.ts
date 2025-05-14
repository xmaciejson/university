import './style.css'
import { calculateExpression, updateExpression, deleteLastCharacter } from './calculator'

const display = document.getElementById('display') as HTMLDivElement
const buttons = document.querySelectorAll('.calculator__btn')
let expression = ''

function updateDisplay() {
  display.textContent = expression || '0'
}

buttons.forEach((btn) => {
  const value = (btn as HTMLButtonElement).dataset.value
  const isEquals = btn.id === 'equals'
  const isClear = btn.id === 'clear'
  const isDelete = btn.id === 'delete'

  btn.addEventListener('click', () => {
    if (isClear) {
      expression = ''
    } else if (isDelete) {
      expression = deleteLastCharacter(expression)
    } else if (isEquals) {
      expression = calculateExpression(expression)
    } else if (value) {
      expression = updateExpression(expression, value)
    }

    updateDisplay()
  })
})

updateDisplay()
