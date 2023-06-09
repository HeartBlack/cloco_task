import { Link} from "react-router-dom"

export default function Dashboard() {
  return (
    <>
			<h2>Welcome to Dashboard page</h2>
			<Link to="/create/new/song">
				Create New song
			</Link>


    </>
  )
}
