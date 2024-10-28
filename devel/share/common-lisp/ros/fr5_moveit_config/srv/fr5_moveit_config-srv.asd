
(cl:in-package :asdf)

(defsystem "fr5_moveit_config-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "GoToPose" :depends-on ("_package_GoToPose"))
    (:file "_package_GoToPose" :depends-on ("_package"))
  ))