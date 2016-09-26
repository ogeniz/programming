(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(blink-cursor-mode nil)
 '(color-theme-is-global t)
 '(column-number-mode t)
 '(delete-selection-mode t)
 '(display-battery-mode t)
 '(display-time-mode t)
 '(dynamic-completion-mode t)
 '(global-linum-mode t)
 '(global-magit-file-mode t)
 '(global-prettify-symbols-mode t)
 '(gud-tooltip-mode t)
 '(icomplete-mode t)
 '(ido-mode (quote both) nil (ido))
 '(make-backup-files nil)
 '(menu-bar-mode nil)
 '(package-selected-packages
   (quote
    (tramp-term tramp-theme switch-window tabbar-ruler bind-key magic-latex-buffer magit magit-tramp ac-math cdlatex latex-extra latex-math-preview latex-pretty-symbols latex-preview-pane latex-unicode-math-mode math-symbol-lists math-symbols auctex auctex-latexmk man-commands auto-compile auto-complete auto-complete-auctex auto-complete-c-headers auto-complete-chunk auto-complete-clang auto-complete-exuberant-ctags auto-complete-octave auto-complete-pcmp pcomplete-extension julia-mode julia-shell color-theme cl-format)))
 '(show-paren-mode t)
 '(size-indication-mode t)
 '(timeclock-mode-line-display t)
 '(tool-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:inherit nil :stipple nil :background "white" :foreground "black" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight bold :height 138 :width normal :foundry "B&H" :family "LucidaTypewriter")))))

(defalias 'yes-or-no-p 'y-or-n-p)

;; Simple package system for Emacs
(require 'package)
(setq load-prefer-newer t)
(setq package-archives '(("gnu" . "http://elpa.gnu.org/packages/")
  ("marmalade" . "http://marmalade-repo.org/packages/")
  ("melpa" . "http://melpa.milkbox.net/packages/")))
(package-initialize)

;; Load Tramp
(require 'tramp)
;; Tramp Term
(require 'tramp-term)


;; Magically enhance LaTeX-mode font-locking for semi-WYSIWYG editing
(require 'magic-latex-buffer)

;; AUCTeX setup
(load "auctex.elc" nil t t)
(load "preview.elc" nil t t)
(setq TeX-auto-save t)
(setq TeX-parse-self t)
(setq-default TeX-master nil)
(setq reftex-plug-into-AUCTeX t)
(add-hook 'LaTeX-mode-hook 'auto-fill-mode)
(add-hook 'LaTeX-mode-hook 'flyspell-mode)
(add-hook 'LaTeX-mode-hook 'LaTeX-math-mode)
(add-hook 'LaTeX-mode-hook 'cdlatex-mode)
(add-hook 'LaTeX-mode-hook 'turn-on-reftex)
(add-hook 'latex-mode-hook 'magic-latex-buffer)
;; ;; Adds several useful functionalities to LaTeX-mode.
(eval-after-load 'LaTeX-mode '(latex/setup-keybinds))
;; ;; Display many latex symbols as their unicode counterparts
(require 'latex-pretty-symbols)

;; Automatically compile Emacs Lisp libraries
(require 'auto-compile)
(auto-compile-on-load-mode)
(auto-compile-on-save-mode)

(require 'auto-complete)
(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "/home/ogeniz/.emacs.d/ac-dict/")
(ac-config-default)

(require 'ac-math) 
(add-to-list 'ac-modes 'latex-mode)   ; make auto-complete aware of `latex-mode`
;; Auto-Completion for auctex
(require 'auto-complete-auctex)
(defun ac-LaTeX-mode-setup () ; add ac-sources to default ac-sources
  (setq ac-sources
	(append '(ac-source-math-unicode ac-source-math-latex ac-source-latex-commands)
		ac-sources)))
(add-hook 'LaTeX-mode-hook 'ac-LaTeX-mode-setup)
(global-auto-complete-mode t)
(setq ac-math-unicode-in-math-p t)

;; Add interactive commands for every manpages installed in your computer.
(require 'man-commands)

(require 'color-theme)
(color-theme-initialize)

(require' pcomplete-extension)

;; A simple way to manage personal keybindings
(require 'bind-key)
(bind-key* "<C-x w>" 'switch-window)
(bind-key "C-c g" 'magit-status)
(bind-key "C-x M-g" 'magit-dispatch-popup)

;; Pretty tabbar, autohide, use both tabbar/rulerPretty tabbar, autohide, use both tabbar/ruler
(require 'tabbar-ruler)
(add-hook 'tabbar-ruler 'tabbar-mode)

;; A *visual* way to choose a window to switch to
(require 'switch-window)

;; XWidgets emacs 25 only
;; make these keys behave like normal browser
;; (define-key xwidget-webkit-mode-map [mouse-4] 'xwidget-webkit-scroll-down)
;; (define-key xwidget-webkit-mode-map [mouse-5] 'xwidget-webkit-scroll-up)
;; (define-key xwidget-webkit-mode-map (kbd "<up>") 'xwidget-webkit-scroll-down)
;; (define-key xwidget-webkit-mode-map (kbd "<down>") 'xwidget-webkit-scroll-up)
;; (define-key xwidget-webkit-mode-map (kbd "M-w") 'xwidget-webkit-copy-selection-as-kill)
;; (define-key xwidget-webkit-mode-map (kbd "C-c") 'xwidget-webkit-copy-selection-as-kill)

;; ;; adapt webkit according to window configuration chagne automatically
;; ;; without this hook, every time you change your window configuration,
;; ;; you must press 'a' to adapt webkit content to new window size
;; (add-hook 'window-configuration-change-hook (lambda ()
;; 					      (when (equal major-mode 'xwidget-webkit-mode)
;; 						(xwidget-webkit-adjust-size-dispatch))))

;; ;; by default, xwidget reuses previous xwidget window,
;; ;; thus overriding your current website, unless a prefix argument
;; ;; is supplied
;; ;;
;; ;; This function always opens a new website in a new window
;; (defun xwidget-browse-url-no-reuse (url &optional sessoin)
;;   (interactive (progn
;;                  (require 'browse-url)
;;                  (browse-url-interactive-arg "xwidget-webkit URL: "
;;                                              )))
;;   (xwidget-webkit-browse-url url t))

;; ;; make xwidget default browser
;; (setq browse-url-browser-function (lambda (url session)
;; 				    (other-window 1)
;; 				    (xwidget-browse-url-no-reuse url)))

;; ac-math            20141116.1327 installed             Auto-complete sources for input of mathematical symbols and latex tags
;; auctex             11.89.5       installed             Integrated environment for *TeX*
;; auctex-latexmk     20160923.7    installed             Add LatexMk support to AUCTeX
;; auto-compile       20160711.1012 installed             automatically compile Emacs Lisp libraries
;; auto-complete      20160827.649  installed             Auto Completion for GNU Emacs
;; auto-complete-a... 20140223.958  installed             auto-completion for auctex
;; auto-complete-c... 20150911.2023 installed             An auto-complete source for C/C++ header files
;; auto-complete-c... 20140225.146  installed             Auto-completion for dot.separated.words.
;; auto-complete-c... 20140409.52   installed             Auto Completion source for clang for GNU Emacs
;; auto-complete-e... 20140320.24   installed             Exuberant ctags auto-complete.el source
;; auto-complete-o... 0.1           installed             Auto-complete for Octave
;; auto-complete-pcmp 20140226.2251 installed             Provide auto-complete sources using pcomplete results
;; bind-key           20160227.48   installed             A simple way to manage personal keybindings
;; cdlatex            20140707.426  installed             Fast input methods for LaTeX environments and math
;; cl-format          20160412.1745 installed             CL format routine.
;; color-theme        20080305.34   installed             install color themes
;; julia-mode         20160803.1643 installed             Major mode for editing Julia source code
;; julia-shell        20160514.728  installed             Major mode for an inferior Julia shell
;; latex-extra        20160328.1721 installed             Adds several useful functionalities to LaTeX-mode.
;; latex-math-preview 20160321.2159 installed             preview LaTeX mathematical expressions.
;; latex-pretty-sy... 20151112.244  installed             Display many latex symbols as their unicode counterparts
;; latex-preview-pane 20151023.1303 installed             Makes LaTeX editing less painful by providing a updatable preview pane
;; latex-unicode-m... 20160708.902  installed             Input method for Unicode math symbols
;; magic-latex-buffer 20160212.603  installed             Magically enhance LaTeX-mode font-locking for semi-WYSIWYG editing
;; magit              20160924.258  installed             A Git porcelain inside Emacs
;; magit-tramp        0.1.0         installed             git method for TRAMP
;; man-commands       20151221.1421 installed             Add interactive commands for every manpages installed in your computer.
;; math-symbol-lists  20160302.1431 installed             Lists of Unicode math symbols and latex commands
;; math-symbols       20151121.1642 installed             Math Symbol Input methods and conversion tools
;; pcomplete-exten... 20140604.947  installed             additional completion for pcomplete
;; switch-window      20160229.334  installed             A *visual* way to choose a window to switch to
;; tabbar-ruler       20160801.2007 installed             Pretty tabbar, autohide, use both tabbar/ruler
;; tramp-term         20141104.1345 installed             Automatic setup of directory tracking in ssh sessions.
;; tramp-theme        0.1.1         installed             Custom theme for remote buffers

