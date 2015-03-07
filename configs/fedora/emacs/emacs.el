;; (add-to-list 'load-path "/home/ogeniz/.emacs.d/")
;; (let ((default-directory "/home/ogeniz/.emacs.d/"))
;;   (normal-top-level-add-subdirs-to-load-path))

(global-set-key [S-f1] 'undo-only)
(global-set-key [S-f2] 'emacs-uptime)
(global-set-key [f5] 'find-file)
(global-set-key [f6] 'disk)    
(global-set-key [M-f5] 'next-buffer)
(global-set-key [S-f5] 'previous-buffer)
(global-set-key [M-f6] 'next-multiframe-window)
(global-set-key [S-f6] 'previous-multiframe-window)
(global-set-key [f7] 'save-buffer)
(global-set-key [f8] 'kill-buffer-and-window)
(global-set-key [f9] 'kill-emacs)
(global-set-key [S-f10] 'lacarte-execute-menu-command)

;; Simplified find-file, revert-file, save-buffer interface
(autoload 'disk "disk" "Save, revert, or find file." t)

;; Enable window-numbering-mode and use M-1 through M-0 to navigate.
(setq window-numbering-assign-func
      (lambda () (when (equal (buffer-name) "*Calculator*") 9)))
;; ispell program name
(setq-default ispell-program-name "aspell")
;; set tabstop 4 spaces
(setq-default indent-tabs-mode nil)
(setq-default tab-width 4)
(setq indent-line-function 'insert-tab)
;; syntax highlighting by default
(global-font-lock-mode t)
;; Changes all yes/no questions to y/n type
(fset 'yes-or-no-p 'y-or-n-p)
;; do not make backup files
(setq make-backup-files nil)
(setq display-time-day-and-date t
    display-time-24hr-format t)
(setq x-alt-keysym 'meta)  ;; setting x-alt-keysym to meta
(set-scroll-bar-mode 'right)   ; replace 'right with 'left to place it to the left
;;
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(auto-complete-mode t)
 '(blink-cursor-mode nil)
 '(c-default-style
   (quote
    ((c-mode . "ellemtel")
     (java-mode . "java")
     (awk-mode . "awk")
     (other . "gnu"))))
 '(column-number-mode t)
 '(cua-mode t nil (cua-base))
 '(default-justification (quote full))
 '(delete-selection-mode t)
 '(display-time-mode t)
 '(dynamic-completion-mode t)
 '(fancy-battery-mode t)
 '(global-cwarn-mode t)
 '(global-linum-mode t)
 '(ido-mode (quote both) nil (ido))
 '(kill-whole-line t)
 '(load-home-init-file t t)
 '(menu-bar-mode nil)
 '(mouse-avoidance-mode (quote banish) nil (avoid))
 '(pending-delete-mode t t)
 '(show-paren-mode t)
 '(size-indication-mode t)
 '(timeclock-mode-line-display t)
 '(tool-bar-mode nil)
 '(uniquify-buffer-name-style (quote forward) nil (uniquify)))
;;
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:inherit nil :stipple nil :background "white" :foreground "black" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight ultra-bold :height 135 :width normal :foundry "b&h" :family "lucidatypewriter"))))
 '(menu ((t (:slant normal :weight normal :height 130 :width normal :foundry "lucidatypewriter" :family "b&h")))))

;; Simple package system for Emacs
(require 'package)
(setq package-archives '(("gnu" . "http://elpa.gnu.org/packages/")
  ("marmalade" . "http://marmalade-repo.org/packages/")
  ("melpa" . "http://melpa.milkbox.net/packages/")))
(package-initialize)
    
;; An interactive tail mode that allows you to filter the tail with
;; unix pipes and highlight the contents of the tailed file. Works
;; locally or on remote files using tramp.
;; M-x itail RET /file/to/tail
(require 'itail)
;; Color Themes
(require 'color-theme)
(color-theme-initialize)
(color-theme-arjen)
        
;; Pretty tabbar, autohide, use both tabbar/ruler
(require 'tabbar-ruler)    

;; Mode for fontification of ~/.ssh/config
(autoload 'ssh-config-mode "ssh-config-mode" t)
(add-to-list 'auto-mode-alist '(".ssh/config\\'"       . ssh-config-mode))
(add-to-list 'auto-mode-alist '("sshd?_config\\'"      . ssh-config-mode))
(add-to-list 'auto-mode-alist '("known_hosts\\'"       . ssh-known-hosts-mode))
(add-to-list 'auto-mode-alist '("authorized_keys2?\\'" . ssh-authorized-keys-mode))
(add-hook 'ssh-config-mode-hook 'turn-on-font-lock)

;; Auto Completion for GNU Emacs
(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "/home/ogeniz/.emacs.d/ac-dict/")
(ac-config-default)
;; ;; An auto-complete source for Octave
;; (require 'ac-octave)
;; (defun ac-octave-mode-setup ()
;; (setq ac-sources '(ac-source-octave)))
;; (add-hook 'octave-mode-hook '(lambda () (ac-octave-mode-setup)))
;; An auto-complete source for C/C++ header files
(require 'auto-complete-c-headers)
(add-hook 'c-mode-hook
            (lambda ()
              (add-to-list 'ac-sources 'ac-source-c-headers)
              (add-to-list 'ac-sources 'ac-source-c-header-symbols t)))
;; (add-to-list 'ac-sources 'ac-source-c-headers)
;; ;; auto-completion for auctex
;; (require 'auto-complete-auctex)
;; Execute menu items as commands, with completion
(require 'lacarte)
;; Load Tramp
(require 'tramp)
(setq tramp-default-method "scp")
;; ;; Integrated environment for *TeX*
;; (load "auctex-pkg.elc" nil t t)
;; (load "preview.elc" nil t t)
;; (setq TeX-auto-save t)
;; (setq TeX-parse-self t)
;; (setq-default TeX-master nil)
;; (add-hook 'LaTeX-mode-hook 'auto-fill-mode)
;; (add-hook 'LaTeX-mode-hook 'flyspell-mode)
;; (add-hook 'LaTeX-mode-hook 'LaTeX-math-mode)
;; (add-hook 'LaTeX-mode-hook 'turn-on-reftex)
;; (setq reftex-plug-into-AUCTeX t)
;; ;; Adds several useful functionalities to LaTeX-mode.
;; (eval-after-load 'LaTeX-mode '(latex/setup-keybinds))
;; ;; Display many latex symbols as their unicode counterparts
;; (require 'latex-pretty-symbols)
