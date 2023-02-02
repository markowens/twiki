#lang racket

(define (extract str)
  (substring str 4 7))

; to use in other modules, use one of the following two lines:
;(provide (all-defined-out))
; or
(provide extract)


