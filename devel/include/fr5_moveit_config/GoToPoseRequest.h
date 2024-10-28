// Generated by gencpp from file fr5_moveit_config/GoToPoseRequest.msg
// DO NOT EDIT!


#ifndef FR5_MOVEIT_CONFIG_MESSAGE_GOTOPOSEREQUEST_H
#define FR5_MOVEIT_CONFIG_MESSAGE_GOTOPOSEREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace fr5_moveit_config
{
template <class ContainerAllocator>
struct GoToPoseRequest_
{
  typedef GoToPoseRequest_<ContainerAllocator> Type;

  GoToPoseRequest_()
    : x(0.0)
    , y(0.0)
    , z(0.0)  {
    }
  GoToPoseRequest_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , z(0.0)  {
  (void)_alloc;
    }



   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef double _z_type;
  _z_type z;





  typedef boost::shared_ptr< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> const> ConstPtr;

}; // struct GoToPoseRequest_

typedef ::fr5_moveit_config::GoToPoseRequest_<std::allocator<void> > GoToPoseRequest;

typedef boost::shared_ptr< ::fr5_moveit_config::GoToPoseRequest > GoToPoseRequestPtr;
typedef boost::shared_ptr< ::fr5_moveit_config::GoToPoseRequest const> GoToPoseRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator1> & lhs, const ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator1> & lhs, const ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace fr5_moveit_config

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4a842b65f413084dc2b10fb484ea7f17";
  }

  static const char* value(const ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4a842b65f413084dULL;
  static const uint64_t static_value2 = 0xc2b10fb484ea7f17ULL;
};

template<class ContainerAllocator>
struct DataType< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fr5_moveit_config/GoToPoseRequest";
  }

  static const char* value(const ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GoToPoseRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fr5_moveit_config::GoToPoseRequest_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<double>::stream(s, indent + "  ", v.z);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FR5_MOVEIT_CONFIG_MESSAGE_GOTOPOSEREQUEST_H
