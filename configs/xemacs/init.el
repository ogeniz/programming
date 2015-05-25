(defun my-toggle-toolbar ()
  (interactive)
  (set-specifier default-toolbar-visible-p
                 (not (specifier-instance default-toolbar-visible-p))))
(global-set-key "\C-xt" 'my-toggle-toolbar)
(global-set-key (kbd "C-x C-b") 'ibuffer)
(autoload 'ibuffer "ibuffer" "List buffers." t)
(global-set-key (kbd "<f6>") 'switch-to-other-buffer) ;; M-C-l
(global-set-key (kbd "<f8>") 'kill-this-buffer)
(global-set-key (kbd "<f9>") 'kill-emacs)
(global-set-key (kbd "<f10>") 'accelerate-menu)
(global-set-key (kbd "<f11>") 'delete-primary-selection)

(load "big-menubar")
(setq options-save-faces t)
(setq make-backup-files nil)
(setq-default font-lock-maximum-decoration t)
(fset 'yes-or-no-p 'y-or-n-p) ; Yes or no prompts accept short y or n
(set-face-background 'default  "Peru") ; frame background color
;;(set-face-background 'default  "Tan") ; frame background color
;;(set-face-background 'default  "Moccasin") ; frame background color
;; (set-face-background 'default  "Gainsboro") ; frame background color

(require 'tex-site)
(setq TeX-auto-save t)
(setq TeX-parse-self t)
(setq-default TeX-master nil)
