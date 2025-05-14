import { evaluate } from 'mathjs'

export function calculateExpression(expression: string): string {
  try {
    // Zamiana przecinka na kropkę przed obliczeniem
    const result = evaluate(expression.replace(',', '.'))
    // Zwracamy wynik z przecinkiem
    return String(result).replace('.', ',')
  } catch {
    return 'Error'
  }
}

export function updateExpression(expression: string, value: string): string {
  if (expression === 'Error') return value
  return expression + value
}

export function deleteLastCharacter(expression: string): string {
  return expression.slice(0, -1)
}
