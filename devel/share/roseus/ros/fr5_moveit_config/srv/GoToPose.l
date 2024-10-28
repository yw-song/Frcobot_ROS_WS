;; Auto-generated. Do not edit!


(when (boundp 'fr5_moveit_config::GoToPose)
  (if (not (find-package "FR5_MOVEIT_CONFIG"))
    (make-package "FR5_MOVEIT_CONFIG"))
  (shadow 'GoToPose (find-package "FR5_MOVEIT_CONFIG")))
(unless (find-package "FR5_MOVEIT_CONFIG::GOTOPOSE")
  (make-package "FR5_MOVEIT_CONFIG::GOTOPOSE"))
(unless (find-package "FR5_MOVEIT_CONFIG::GOTOPOSEREQUEST")
  (make-package "FR5_MOVEIT_CONFIG::GOTOPOSEREQUEST"))
(unless (find-package "FR5_MOVEIT_CONFIG::GOTOPOSERESPONSE")
  (make-package "FR5_MOVEIT_CONFIG::GOTOPOSERESPONSE"))

(in-package "ROS")





(defclass fr5_moveit_config::GoToPoseRequest
  :super ros::object
  :slots (_x _y _z ))

(defmethod fr5_moveit_config::GoToPoseRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass fr5_moveit_config::GoToPoseResponse
  :super ros::object
  :slots (_success ))

(defmethod fr5_moveit_config::GoToPoseResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass fr5_moveit_config::GoToPose
  :super ros::object
  :slots ())

(setf (get fr5_moveit_config::GoToPose :md5sum-) "14fb54e9e518f55d418823395ca25d0b")
(setf (get fr5_moveit_config::GoToPose :datatype-) "fr5_moveit_config/GoToPose")
(setf (get fr5_moveit_config::GoToPose :request) fr5_moveit_config::GoToPoseRequest)
(setf (get fr5_moveit_config::GoToPose :response) fr5_moveit_config::GoToPoseResponse)

(defmethod fr5_moveit_config::GoToPoseRequest
  (:response () (instance fr5_moveit_config::GoToPoseResponse :init)))

(setf (get fr5_moveit_config::GoToPoseRequest :md5sum-) "14fb54e9e518f55d418823395ca25d0b")
(setf (get fr5_moveit_config::GoToPoseRequest :datatype-) "fr5_moveit_config/GoToPoseRequest")
(setf (get fr5_moveit_config::GoToPoseRequest :definition-)
      "float64 x
float64 y
float64 z
---
bool success

")

(setf (get fr5_moveit_config::GoToPoseResponse :md5sum-) "14fb54e9e518f55d418823395ca25d0b")
(setf (get fr5_moveit_config::GoToPoseResponse :datatype-) "fr5_moveit_config/GoToPoseResponse")
(setf (get fr5_moveit_config::GoToPoseResponse :definition-)
      "float64 x
float64 y
float64 z
---
bool success

")



(provide :fr5_moveit_config/GoToPose "14fb54e9e518f55d418823395ca25d0b")


